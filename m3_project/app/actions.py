from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow, UserEditWindow
from .controller import observer


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    add_to_desktop = True

    add_window = ModelEditWindow.fabricate(model=model)
    edit_window = ModelEditWindow.fabricate(model=model)


class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    add_to_desktop = True

    edit_window = UserEditWindow
    add_window = UserAddWindow


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    add_to_desktop = True

    add_window = ModelEditWindow.fabricate(model=model)

    edit_window = ModelEditWindow.fabricate(model=model)


class PermissionPack(ObjectPack):
    model = Permission

    add_to_menu = True
    add_to_desktop = True

    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer
    )
