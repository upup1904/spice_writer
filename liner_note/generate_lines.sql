WITH lines as (
     select generate_series as line_no from
     generate_series(1,5000)
),
epis as (
     select generate_series as epi
     from generate_series(1,20)
),
FEEDME as (
select epi, line_no, epi::text || '.' || line_no::text as slug
       from lines
       	    join epis
	    on CASE 
	    WHEN EPI = 1 AND line_no < 745 then True
	    WHEN EPI = 2 AND line_no < 450 then True
	    WHEN EPI = 3 AND line_no < 556 then True
	    WHEN EPI = 4 AND line_no < 552 then True
	    WHEN EPI = 5 AND line_no < 573 then True
	    WHEN EPI = 6 AND line_no < 1034 then True
	    WHEN EPI = 7 AND line_no < 1176 then True
	    WHEN EPI = 8 AND line_no < 1194 then True
	    WHEN EPI = 9 AND line_no < 1226 then True
	    WHEN EPI = 10 AND line_no < 1283 then True
	    WHEN EPI = 11 AND line_no < 1295 then True
	    WHEN EPI = 12 AND line_no < 1919 then True
	    WHEN EPI = 13 AND line_no < 1307 then True
	    WHEN EPI = 14 AND line_no < 1592 then True
	    WHEN EPI = 15 AND line_no < 4968 then True
	    WHEN EPI = 16 AND line_no < 1895 then True
	    WHEN EPI = 17 AND line_no < 2333 then True
	    WHEN EPI = 18 AND line_no < 1612 then True
	    ELSE False END
	    )
INSERT into liner_note_line(episode, line, slug)
SELECT epi, line_no, slug FROM FEEDME
;

