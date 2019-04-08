use registration;

SELECT tweets.id, tweets.tweet, tweets.created_at, tweets.users_id, CONCAT(users.first_name, ' ', users.last_name) as user_name, 
	   count(tweets_id) as likes,
       follows.follower_id
FROM users 
LEFT JOIN tweets on users.id = tweets.users_id 
LEFT JOIN likes on tweets.id = likes.tweets_id
LEFT JOIN follows on users.id = follows.users_id
WHERE tweets.id IS NOT NULL 
ORDER BY tweets.created_at desc;

select * from tweets;
select * from follows;