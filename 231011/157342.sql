--https://school.programmers.co.kr/learn/courses/30/lessons/157341


SELECT DISTINCT(CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR 
WHERE CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE EXTRACT(MONTH FROM START_DATE)=10
)
AND CAR_TYPE='세단'
ORDER BY CAR_ID DESC