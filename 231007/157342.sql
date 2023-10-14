-- https://school.programmers.co.kr/learn/courses/30/lessons/157342

SELECT CAR_ID, ROUND(AVG(END_DATE-START_DATE+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING ROUND(AVG(END_DATE-START_DATE+1),1)>=7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC