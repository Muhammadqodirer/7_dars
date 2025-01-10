from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = "Mening Loyiham"
    site_title = "Admin Panel"
    index_title = "Boshqaruv"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_admin.css'
        return context

admin.site = CustomAdminSite()
