from django import forms
from django.core.validators import MinValueValidator


class UpdatePharmacy(forms.Form):
    city = forms.CharField(max_length=50, label="", required=None,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Город(не обязательно)'}))
    district = forms.CharField(max_length=50, label="", required=None,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Район(не обязательно)'}))
    street = forms.CharField(max_length=50, label="", required=None,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'placeholder': 'Улица(не обязательно)'}))
    index = forms.CharField(max_length=50, label="", required=None,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'Индекс(не обязательно)'}))
    phone = forms.CharField(max_length=50, label="", required=None,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'Телефон(не обязательно)'}))


class AddSeller(forms.Form):
    name = forms.CharField(max_length=50, label="",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=50, label="",
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Фамилия'}))
    fathername = forms.CharField(max_length=50, label="",
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control my-1', 'placeholder': 'Отчество'}))
    phone = forms.CharField(max_length=50, label="", required=None,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'Телефон(не обязательно)'}))
    login = forms.EmailField(max_length=50, label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'autocomplete': 'off', 'placeholder': 'Логин'}))
    password = forms.CharField(max_length=50, label="",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control my-1', 'autocomplete': 'off',
                                          'placeholder': 'Пароль'}))


class DeleteSeller(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для удаления'}))


class UpdateSeller(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для изменения'}))
    name = forms.CharField(max_length=50, label="", required=None,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=50, label="", required=None,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Фамилия'}))
    fathername = forms.CharField(max_length=50, label="", required=None,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control my-1', 'placeholder': 'Отчество'}))
    phone = forms.CharField(max_length=50, label="", required=None,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'Телефон(не обязательно)'}))
    login = forms.EmailField(max_length=50, label="", required=None,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'autocomplete': 'off', 'placeholder': 'Логин'}))
    password = forms.CharField(max_length=50, label="", required=None,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control my-1', 'autocomplete': 'off',
                                          'placeholder': 'Пароль'}))


class RecipeSearchDate(forms.Form):
    expiredate = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'],
                                 widget=forms.DateTimeInput(
                                     attrs={'data-target': '#datetimepicker1',
                                            'class': 'form-control date datetimepicker-input my-1',
                                            'placeholder': 'Срок годности', 'id': "datetimepicker1",
                                            'data-target-input': 'nearest'}))


class RecipeSearchDoctor(forms.Form):
    doctor = forms.CharField(max_length=50, label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'placeholder': 'Доктор'}))


class DeleteRecipe(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для удаления'}))


class AddRecipe(forms.Form):
    doctor = forms.CharField(max_length=50, label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'placeholder': 'Доктор'}))
    signature = forms.CharField(max_length=50, label="",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control my-1', 'placeholder': 'Подпись'}))

    expiredate = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'],
                                 widget=forms.DateTimeInput(
                                     attrs={'data-target': '#datetimepicker2',
                                            'class': 'form-control date datetimepicker-input my-1',
                                            'placeholder': 'Срок годности', 'id': "datetimepicker2",
                                            'data-target-input': 'nearest'}))


class UpdateRecipe(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для изменения'}))
    doctor = forms.CharField(max_length=50, label="", required=None,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control my-1', 'placeholder': 'Доктор'}))
    signature = forms.CharField(max_length=50, label="", required=None,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control my-1', 'placeholder': 'Подпись'}))

    expiredate = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'], required=None,
                                 widget=forms.DateTimeInput(
                                     attrs={'data-target': '#datetimepicker3',
                                            'class': 'form-control date datetimepicker-input my-1',
                                            'placeholder': 'Срок годности', 'id': "datetimepicker3",
                                            'data-target-input': 'nearest'}))


class PillSearchDate(forms.Form):
    expire_date = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'],
                                  widget=forms.DateTimeInput(
                                      attrs={'data-target': '#datetimepicker4',
                                             'class': 'form-control date datetimepicker-input my-1',
                                             'placeholder': 'Годен до', 'id': "datetimepicker4",
                                             'data-target-input': 'nearest'}))


class PillSearchName(forms.Form):
    pill_name = forms.CharField(max_length=50, label="",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control my-1', 'placeholder': 'Наименование'}))
    is_search_global = forms.BooleanField(label="Поиск по всем аптекам", required=None, widget=forms.CheckboxInput(
        attrs={'class': 'm-3', 'placeholder': 'Поиск по всем аптекам'}
    ))


class PillSearchCategory(forms.Form):
    category = forms.CharField(max_length=15, label="",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Категория'}))
    is_search_global = forms.BooleanField(label="Поиск по всем аптекам", required=None, widget=forms.CheckboxInput(
        attrs={'class': 'm-3', 'placeholder': 'Поиск по всем аптекам'}
    ))


class PillSearchCost(forms.Form):
    start_cost = forms.IntegerField(label="",
                                    widget=forms.NumberInput(
                                        attrs={'class': 'form-control my-1', 'placeholder': 'Начальная цена'}))
    end_cost = forms.IntegerField(label="",
                                  widget=forms.NumberInput(
                                      attrs={'class': 'form-control my-1', 'placeholder': 'Конечная цена'}))


class AddPill(forms.Form):
    name = forms.CharField(max_length=50, label="",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Наименование'}))

    cost = forms.IntegerField(label="", validators=[MinValueValidator(0)],
                              widget=forms.NumberInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Цена'}))

    category = forms.CharField(max_length=15, label="", required=None,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Категория'}))

    country = forms.CharField(max_length=20, label="", required=None,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Страна'}))

    barcode = forms.CharField(max_length=30, label="", required=None,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Штрихкод'}))

    recipe_id = forms.IntegerField(label="", required=None,
                                   widget=forms.NumberInput(
                                       attrs={'class': 'form-control my-1', 'placeholder': 'ID рецепта'}))

    info = forms.CharField(max_length=3000, label="", required=None,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Информация'}))

    reg_date = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'],
                               widget=forms.DateTimeInput(
                                   attrs={'data-target': '#datetimepicker5',
                                          'class': 'form-control date datetimepicker-input my-1',
                                          'placeholder': 'Дата поставки', 'id': "datetimepicker5",
                                          'data-target-input': 'nearest'}))

    end_date = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'], required=None,
                               widget=forms.DateTimeInput(
                                   attrs={'data-target': '#datetimepicker6', 'cols': 50,
                                          'class': 'form-control date datetimepicker-input my-1',
                                          'placeholder': 'Годен до', 'id': "datetimepicker6",
                                          'data-target-input': 'nearest'}))


class UpdatePill(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для изменения'}))
    name = forms.CharField(max_length=50, label="", required=None,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Наименование'}))

    cost = forms.IntegerField(label="", required=None,
                              widget=forms.NumberInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Цена'}))

    category = forms.CharField(max_length=15, label="", required=None,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Категория'}))

    country = forms.CharField(max_length=20, label="", required=None,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Страна'}))

    barcode = forms.CharField(max_length=30, label="", required=None,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control my-1', 'placeholder': 'Штрихкод'}))

    recipe_id = forms.IntegerField(label="", required=None,
                                   widget=forms.NumberInput(
                                       attrs={'class': 'form-control my-1', 'placeholder': 'ID рецепта'}))

    info = forms.CharField(max_length=3000, label="", required=None,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control my-1', 'placeholder': 'Информация'}))

    reg_date = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'], required=None,
                               widget=forms.DateTimeInput(
                                   attrs={'data-target': '#datetimepicker7',
                                          'class': 'form-control date datetimepicker-input my-1',
                                          'placeholder': 'Дата поставки', 'id': "datetimepicker7",
                                          'data-target-input': 'nearest'}))

    end_date = forms.DateField(label="", input_formats=['%d/%m/%Y %H:%M'], required=None,
                               widget=forms.DateTimeInput(
                                   attrs={'data-target': '#datetimepicker8',
                                          'class': 'form-control date datetimepicker-input my-1',
                                          'placeholder': 'Годен до', 'id': "datetimepicker8",
                                          'data-target-input': 'nearest'}))


class DeletePill(forms.Form):
    id = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для удаления'}))


class StorageSearchId(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для поиска'}))


class AddStorage(forms.Form):
    pillId = forms.IntegerField(label="",
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control my-1', 'placeholder': 'ID препарата'}))

    count = forms.IntegerField(label="",
                               widget=forms.NumberInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Количество'}))


class UpdateStorage(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для изменения'}))

    pillId = forms.IntegerField(label="", required=None,
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control my-1', 'placeholder': 'ID препарата'}))

    count = forms.IntegerField(label="", required=None,
                               widget=forms.NumberInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Количество'}))


class DeleteStorage(forms.Form):
    ID = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для удаления'}))


class AddPillToBasket(forms.Form):
    id = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для добавления'}))
    count = forms.IntegerField(label="",
                               widget=forms.NumberInput(
                                   attrs={'class': 'form-control my-1', 'placeholder': 'Количество'}))


class RecipeSearchId(forms.Form):
    id = forms.IntegerField(label="",
                            widget=forms.NumberInput(
                                attrs={'class': 'form-control my-1', 'placeholder': 'ID для поиска'}))
