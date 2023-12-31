SELECT R.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, R.SCORE
FROM REST_INFO I
JOIN(
SELECT A.REST_ID, ROUND(AVG(B.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO A JOIN REST_REVIEW B ON A.REST_ID=B.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY A.REST_ID)R ON I.REST_ID=R.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC