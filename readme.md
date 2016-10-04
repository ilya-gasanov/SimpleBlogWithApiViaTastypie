    This simple blog site was built on the basis Harrison Kinsley`s video tutorial 
    (you can watch it here https://www.youtube.com/user/sentdex/videos)

    I have added base API functions via Tastypie,
    they can be used at - site/api/v1/blog  (list of posts,post create)
                    - site/api/v1/blog/post_id (edit, 
                                                detail view, delete).
     Fields body,title, date are required to create a post.
    Only authorized users can manipulate with api functions
    It runs as standard on the Django`s test server
    Please, run python manage.py migrate --run-syncdb before first start.
    Django admin interface can be used to add posts to the blog.