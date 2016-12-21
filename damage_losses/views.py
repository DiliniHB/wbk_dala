from django.shortcuts import render
from settings.models import District, Province
from incidents.models import IncidentReport
import yaml, json
from django.http import HttpResponse
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core import serializers
from django.conf import settings


def dl_health_damagelost_other_medical_facilities(request):
    districts = District.objects.all()
    incidents = IncidentReport.objects.all()

    context = {
        'districts': districts,
        'incidents': incidents
    }
    return render(request, 'damage_losses/health_damagelost_other_medi.html', context)


#dileepa
def health_damagelost_ministry_helth(request):
    districts = District.objects.all()
    provinces = Province.objects.all()
    context = {
        'districts': districts,
        'provinces': provinces,
    }
    return render(request, 'damage_losses/health_damagelost_ministry_helth.html', context)


def health_damagelost_private(request):
    districts = District.objects.all()
    provinces = Province.objects.all()
    context = {
        'districts': districts,
        'provinces': provinces,
    }
    return render(request, 'damage_losses/health_damagelost_private.html', context)


#Sachie
def dl_health_other_medical_facilities(request):
    districts = District.objects.all()
    incidents = IncidentReport.objects.all()
    context = {
        'districts': districts,
        'incidents': incidents,
    }
    return render(request, 'damage_losses/health_damagelost_other_medi.html', context)


def dl_health_summary_sector_district(request):
    districts = District.objects.all()
    incidents = IncidentReport.objects.all()
    context = {
        'districts': districts,
        'incidents': incidents,
    }
    return render(request, 'damage_losses/health_summery_damageloss_dis.html', context)


def dl_health_summary_damage_nationwide(request):
    districts = District.objects.all()
    incidents = IncidentReport.objects.all()
    context = {
        'districts': districts,
        'incidents': incidents,
    }
    return render(request, 'damage_losses/health_summery_damageloss_national.html', context)



@csrf_exempt
def dl_save_data(request):
    dl_data = (yaml.safe_load(request.body))
    dl_table_data = dl_data['table_data']
    com_data = dl_data['com_data']
    todate = timezone.now()
    is_edit = dl_data['is_edit']

    if not is_edit:
        try:
            for interface_table in dl_table_data:
                print 'interface table', ' -->', interface_table, '\n'
                for db_table in dl_table_data[interface_table]:

                    print 'db table', ' -->', db_table, '\n'

                    for row in dl_table_data[interface_table][db_table]:

                        model_class = apps.get_model('damage_losses', db_table)
                        model_object = model_class()

                        # assigning common properties to model object
                        model_object.created_date = todate
                        model_object.lmd = todate
                        if interface_table == 'Table_9':
                            model_object.province_id = com_data['province']
                        elif interface_table == 'Table_10':
                            print 'Table 10'
                        else:
                            model_object.district_id = com_data['district']
                        model_object.incident_id = com_data['incident']

                        print 'row', ' --> ', row, '\n', ' object '

                        for property in row:
                            setattr(model_object, property, row[property])

                            print 'property ', ' --> ', property, ' db_property ', row[property], ' index ', '\n'
                            model_object.save()

        except Exception as e:
            return HttpResponse(e)

    else:
        dl_save_edit_data(dl_table_data, com_data)

    return HttpResponse('success')


@csrf_exempt
def dl_get_data(request):
    data = (yaml.safe_load(request.body))
    com_data = data['com_data']
    incident_id = com_data['incident']
    district = com_data['district']
    db_tables = data['db_tables']

    dl_mtable_data = {}

    for db_table in db_tables:
        model_class = apps.get_model('damage_losses', db_table)
        dl_mtable_data[db_table] = serializers.serialize('json', model_class.objects.filter(incident=incident_id, district=district).order_by('id'))

    return HttpResponse(
        json.dumps(dl_mtable_data),
        content_type='application/javascript; charset=utf8'
    )


@csrf_exempt
def dl_fetch_edit_data(request):

    data = (yaml.safe_load(request.body))
    table_name = data['table_name']
    com_data = data['com_data']
    incident = com_data['incident']
    tables = settings.TABLE_PROPERTY_MAPPER[table_name]

    if table_name == 'Table_9':
        admin_area = com_data['province']
        filter_fields = {'incident': incident, 'province': admin_area}
    else:
        admin_area = com_data['district']
        filter_fields = {'incident': incident, 'district': admin_area}

    bs_mtable_data = {table_name: {}}

    for table in tables:
        table_fields = tables[table]
        model_class = apps.get_model('damage_losses', table)
        bs_mtable_data[table_name][table] = list(model_class.objects.
                                                 filter(**filter_fields).
                                                 values(*table_fields))

    return HttpResponse(
        json.dumps(bs_mtable_data),
        content_type='application/javascript; charset=utf8'
    )


@csrf_exempt
def dl_save_edit_data(table_data, com_data):

    #incident = com_data['incident']
    #district = com_data['district']

    for interface_table in table_data:
        print 'interface table', ' -->', interface_table, '\n'
        for db_table in table_data[interface_table]:

            print 'db table', ' -->', db_table, '\n'

            for row in table_data[interface_table][db_table]:

                model_class = apps.get_model('damage_losses', db_table)
                model_object = model_class.objects.filter(id=row['id'])
                model_object.update(**row)

                print 'row', ' --> ', row, ' id ', model_object[0].id, '\n'


