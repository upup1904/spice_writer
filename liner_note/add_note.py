"""Functions to hande add_note response"""
from .models import Line, LinerNote
from .forms import NoteForm
import re
import logging
from time import gmtime, strftime


logger = logging.getLogger("liner_note")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def process_form(uf: NoteForm):
    note_text = uf.cleaned_data['body']
    user_line_spec = uf.cleaned_data['lines']
    logger.debug(f"line spec is {user_line_spec}")
    new_note = LinerNote()
    new_note.body = note_text
    new_note.title = "Sample title"
    new_note.slug = "Ick slug" + strftime("%Y%b%d%H%M%S", gmtime())
    try:
        new_note.save()
    except Exception as e:
        raise e
    lines, msgs = process_spec(user_line_spec)
    logger.info(f"added note text")
    for x in lines:
        add_to_me = Line.objects.filter(episode=x[0], line=x[1]).get()
        add_to_me.liner_notes.add(new_note)
        try:
            add_to_me.save()
        except Exception as e:
            raise e
    return


def process_spec(user_string):
    msgs = []  # to display to a web browser, warnings
    try:
        m = re.findall('[0-9]+\\.[0-9]+', user_string)
        retval = set()
        for pair in [x.split('.') for x in m]:
            retval.add((int(pair[0]), int(pair[1])))
        for spec in re.findall('[0-9]+\\.[0-9]+-[0-9]+', user_string):
            epi, lines = spec.split('.')
            epi = int(epi)
            start, stop = lines.split('-')
            start, stop = int(start), int(stop)
            if start > stop:
                msgs.append(f"range {spec} is invalid, using first line only")
                # implementation convenience: it is found by the simple regex
                break
            for line in range(start, stop+1):
                retval.add((epi, line))
        return (retval, msgs)
    except Exception as e:
        raise Exception(f'TODO custom {e}')
