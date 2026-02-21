import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

try:
    django.setup()
    print("✅ Django carga OK")
except Exception as e:
    print(f"❌ Error en Django setup: {e}")

try:
    from pages.models import Post
    print("✅ Modelo Post OK")
except Exception as e:
    print(f"❌ Error en Post: {e}")

try:
    from accounts.models import Profile
    print("✅ Modelo Profile OK")
except Exception as e:
    print(f"❌ Error en Profile: {e}")

try:
    from messaging.models import Message
    print("✅ Modelo Message OK")
except Exception as e:
    print(f"❌ Error en Message: {e}")

try:
    from pages import urls as pages_urls
    print("✅ URLs de pages OK")
except Exception as e:
    print(f"❌ Error en URLs pages: {e}")

try:
    from accounts import urls as accounts_urls
    print("✅ URLs de accounts OK")
except Exception as e:
    print(f"❌ Error en URLs accounts: {e}")

try:
    from messaging import urls as messaging_urls
    print("✅ URLs de messaging OK")
except Exception as e:
    print(f"❌ Error en URLs messaging: {e}")