from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django import forms
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow, UserEditWindow, GroupAddWindow, PermissionAddWindow, PermissionEditWindow


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

    add_window = PermissionAddWindow
    edit_window = PermissionEditWindow

    def save_row(self, obj, create_new, request, context):
        s = obj
        content_type = ContentType.objects.get(id=int(request.POST['content_type']))
        obj.content_type  = content_type

        super(PermissionPack, self).save_row(obj, create_new, request, context)
