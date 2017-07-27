def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    # relevant routes for the blog post
    config.add_route('single_user', '/single_user/{user_id}')
    config.add_route('all_users', '/all_users')
    config.add_route('create_new_user', '/create_new_user')
    config.add_route('delete_user', '/delete_user/{user_id}')
    config.add_route('update_user', '/update_user/{user_id}')
