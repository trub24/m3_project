from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from django.contrib.auth.models import User, Group, Permission

from django.contrib.auth.models import User


class UserAddWindow(BaseEditWindow):
    """
    Окно для редактирования и добавления пользователей.
    """
    def _init_components(self):
        """
        Инициализация компонентов окна.
        """
        super(UserAddWindow, self)._init_components()

        self.field__passwoed = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%'

        )
        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last_login',
            format='d.m.Y',
            anchor='100%'
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label='superuser status',
            name='is_superuser',
            anchor='100%'
        )

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field__first_name = ext.ExtStringField(
            label='first name',
            name='first_name',
            allow_blank=True,
            anchor='100%'
        )

        self.field__last_name = ext.ExtStringField(
            label='last name',
            name='last_name',
            allow_blank=True,
            anchor='100%'
        )

        self.field__email = ext.ExtStringField(
            label='email addres',
            name='email',
            allow_blank=True,
            anchor='100%'
        )

        self.field__is_staff = ext.ExtCheckBox(
            label='staff status',
            name='is_staff',
            anchor='100%'
        )
        self.field__is_active = ext.ExtCheckBox(
            label='active',
            name='is_active',
            anchor='100%'
        )

        self.field__date_joined = ext.ExtDateField(
            label='date joined',
            name='date_joined',
            format='d.m.Y',
            anchor='100%',
        )

    def _do_layout(self):
        """
        Размещение компонентов в окне.
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend([
            self.field__passwoed,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ])

    def set_params(self, params):
        """
        Установка параметров окна создания пользователя.
        """
        super(UserAddWindow, self).set_params(params)
        self.params = params
        self.title = 'Создание пользователя'
        self.height = 'auto'


class UserEditWindow(UserAddWindow):
    def set_params(self, params):
        """
        Установка параметров окна редактирования пользователя.
        """
        super(UserAddWindow, self).set_params(params)
        self.params = params
        self.title = 'Редактирование пользователя'
        self.height = 'auto'


class GroupAddWindow(BaseEditWindow):
    def _init_components(self):
        """
        Инициализация компонентов окна.
        """
        super(GroupAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label='name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        codenames = [(perm.codename, perm.codename) for perm in Permission.objects.all()]

        self.field__codename = make_combo_box(
            label='Codename',
            name='codename',
            allow_blank=False,
            anchor='100%',
            data=codenames
        )

    def _do_layout(self):
        """
        Размещение компонентов в окне.
        """
        super(GroupAddWindow, self)._do_layout()
        self.form.items.extend([
            self.field__username,
            self.field__codename,
        ])

    def set_params(self, params):
        """
        Установка параметров окна создания группы.
        """
        super(GroupAddWindow, self).set_params(params)
        self.params = params
        self.title = 'Create group'
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):
    def _init_components(self):
        """
        Инициализация компонентов окна.
        """
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='Name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        self.field__codename = ext.ExtStringField(
            label='Codename',
            name='codename',
            allow_blank=False,
            anchor='100%',
        )

        self.field__content_type = make_combo_box(
            label='Content Type',
            name='content_type',
            allow_blank=False,
            anchor='100%',
            data=[(ct.id, ct.name) for ct in ContentType.objects.all()],
            value_field='id',
            display_field='name'
        )

    def _do_layout(self):
        """
        Размещение компонентов в окне.
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend([
            self.field__name,
            self.field__codename,
            self.field__content_type
        ])

    def set_params(self, params):
        """
        Параметры окна.
        """
        super(PermissionAddWindow, self).set_params(params)
        self.title = 'Add Permission'
        self.width = 400
        self.height = 'auto'


class PermissionEditWindow(PermissionAddWindow):
    def set_params(self, params):
        """
        Параметры окна.
        """
        super(PermissionAddWindow, self).set_params(params)
        self.title = 'Edit Permission'
        self.width = 400
        self.height = 'auto'
