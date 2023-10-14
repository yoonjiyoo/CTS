--https://school.programmers.co.kr/learn/courses/30/lessons/131536#

-- 첫 풀이
SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID FROM ONLINE_SALE GROUP BY USER_ID HAVING COUNT(USER_ID)>=2)
GROUP BY USER_ID,PRODUCT_ID
HAVING COUNT(PRODUCT_ID)>=2
ORDER BY USER_ID,PRODUCT_ID DESC

--10/11 두번째 풀이
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID)>=2 AND COUNT(USER_ID)>=2
ORDER BY USER_ID ASC, PRODUCT_ID DESC