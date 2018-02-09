def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config['ENABLED_MODULES']:
        try:
            import_module('.%s.models' % module_name, package=__name__)
        except Exception as ex:
            pass

    for module_name in app.config['ENABLED_MODULES']:
        import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)
