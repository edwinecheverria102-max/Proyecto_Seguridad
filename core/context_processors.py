from types import SimpleNamespace


def user_context(request):
    """Expone un objeto con la API mínima que usa el template para usuarios autenticados manualmente."""
    session = request.session
    session_user_id = session.get('user_id')
    if session_user_id:
        user = SimpleNamespace(
            is_authenticated=True,
            is_anonymous=False,
            id=session_user_id,
            username=session.get('user_name', 'Usuario'),
            email=session.get('user_email', ''),
            get_full_name=lambda: session.get('user_name', 'Usuario')
        )
        return {'user': user}

    if hasattr(request, 'user') and getattr(request.user, 'is_authenticated', False):
        return {'user': request.user}

    user = SimpleNamespace(
        is_authenticated=False,
        is_anonymous=True,
        id=None,
        username='',
        email='',
        get_full_name=lambda: ''
    )
    return {'user': user}
