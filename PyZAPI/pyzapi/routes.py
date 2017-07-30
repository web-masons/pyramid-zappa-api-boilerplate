def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    # relevant routes for the blog post
    config.add_route('single_user', '/user/{user_id}')
    config.add_route('all_users', '/users')
    config.add_route('create_new_user', '/user/new/{first_name}/{last_name}')
    config.add_route('delete_user', '/user/delete/{user_id}')
    config.add_route('update_user', '/user/update/{user_id}/{first_name}/{last_name}')
