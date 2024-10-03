from pops.POPMSA006_mongo_models import POPMSA006, TemporaryPOPMSA006, TodayPOPMSA006, Last7DaysPOPMSA006, Last30DaysPOPMSA006, ThisYearPOPMSA006

import logging
logger = logging.getLogger(__name__)

from datetime import datetime
import pytz

def popmsa006_mongo_create(data, topic):
    popms_data = {}

    # Flatten the list of dictionaries into a single dictionary
    for dic in data:
        for key, value in dic.items():
            popms_data[key] = value

    timestamp = popms_data.get('timestamp', None)
    utc_time = pytz.utc.localize(datetime.now()) if timestamp is None else pytz.utc.localize(datetime.fromtimestamp(timestamp))
    dhaka_tz = pytz.timezone('Asia/Dhaka')
    # print(f'--------------------Local Time: {utc_time}')
    # print(f'--------------------Local Time: {utc_time.astimezone(dhaka_tz)}')

    popmsa006_mongo = POPMSA006.objects.create(
        created_time=utc_time.astimezone(dhaka_tz),
        topic=topic,
        dev_ID=popms_data.get('dev_ID', None),
        ac_temp_1=popms_data.get('ac_temp_1', None),
        ac_temp_2=popms_data.get('ac_temp_2', None),
        env_temp_1=popms_data.get('env_temp_1', None),
        env_hum_1=popms_data.get('env_hum_1', None),
        env_dp_1=popms_data.get('env_dp_1', None),
        env_temp_2=popms_data.get('env_temp_2', None),
        env_hum_2=popms_data.get('env_hum_2', None),
        env_dp_2=popms_data.get('env_dp_2', None),
        door_state_1=popms_data.get('door_state_1', None),
        door_state_2=popms_data.get('door_state_2', None),
        smoke_state=popms_data.get('smoke_state', None),
        ua=popms_data.get('ua', None),
        ub=popms_data.get('ub', None),
        uc=popms_data.get('uc', None),
        avln=popms_data.get('avln', None),
        uab=popms_data.get('uab', None),
        ubc=popms_data.get('ubc', None),
        uca=popms_data.get('uca', None),
        avll=popms_data.get('avll', None),
        ia=popms_data.get('ia', None),
        ib=popms_data.get('ib', None),
        ic=popms_data.get('ic', None),
        avc=popms_data.get('avc', None),
        pa=popms_data.get('pa', None),
        pb=popms_data.get('pb', None),
        pc=popms_data.get('pc', None),
        sa=popms_data.get('sa', None),
        sb=popms_data.get('sb', None),
        sc=popms_data.get('sc', None),
        qa=popms_data.get('qa', None),
        qb=popms_data.get('qb', None),
        qc=popms_data.get('qc', None),
        totkw=popms_data.get('totkw', None),
        totkva=popms_data.get('totkva', None),
        totkvar=popms_data.get('totkvar', None),
        pfa=popms_data.get('pfa', None),
        pfb=popms_data.get('pfb', None),
        pfc=popms_data.get('pfc', None),
        avpf=popms_data.get('avpf', None),
        f=popms_data.get('f', None),
        totnkwh=popms_data.get('totnkwh', None),
        totnkvah=popms_data.get('totnkvah', None),
        totnkvarh=popms_data.get('totnkvarh', None),
        timestamp=popms_data.get('timestamp', None),
    )

    logger.info(f"mongo_db = POPMSA006, topic = {topic} created {popmsa006_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in POPMSA006------------------------------!>')

    temp_popmsa006_mongo = TemporaryPOPMSA006.objects.create(
        # _id = mongo_models.ObjectIdField(),
        created_time = utc_time.astimezone(dhaka_tz),
        topic = topic,
        dev_ID = popms_data.get('dev_ID', None),
        ac_temp_1 = popms_data.get('ac_temp_1', None),
        ac_temp_2 = popms_data.get('ac_temp_2', None),
        env_temp_1 = popms_data.get('env_temp_1', None),
        env_hum_1 = popms_data.get('env_hum_1', None),
        env_dp_1 = popms_data.get('env_dp_1', None),
        env_temp_2 = popms_data.get('env_temp_2', None),
        env_hum_2 = popms_data.get('env_hum_2', None),
        env_dp_2 = popms_data.get('env_dp_2', None),
        door_state_1 = popms_data.get('door_state_1', None),
        door_state_2 = popms_data.get('door_state_2', None),
        smoke_state = popms_data.get('smoke_state', None),
        ua = popms_data.get('ua', None),
        ub = popms_data.get('ub', None),
        uc = popms_data.get('uc', None),
        avln = popms_data.get('avln', None),
        uab = popms_data.get('uab', None),
        ubc = popms_data.get('ubc', None),
        uca = popms_data.get('uca', None),
        avll = popms_data.get('avll', None),
        ia = popms_data.get('ia', None),
        ib = popms_data.get('ib', None),
        ic = popms_data.get('ic', None),
        avc = popms_data.get('avc', None),
        pa = popms_data.get('pa', None),
        pb = popms_data.get('pb', None),
        pc = popms_data.get('pc', None),
        sa = popms_data.get('sa', None),
        sb = popms_data.get('sb', None),
        sc = popms_data.get('sc', None),
        qa = popms_data.get('qa', None),
        qb = popms_data.get('qb', None),
        qc = popms_data.get('qc', None),
        totkw = popms_data.get('totkw', None),
        totkva = popms_data.get('totkva', None),
        totkvar = popms_data.get('totkvar', None),
        pfa = popms_data.get('pfa', None),
        pfb = popms_data.get('pfb', None),
        pfc = popms_data.get('pfc', None),
        avpf = popms_data.get('avpf', None),
        f = popms_data.get('f', None),
        totnkwh = popms_data.get('totnkwh', None),
        totnkvah = popms_data.get('totnkvah', None),
        totnkvarh = popms_data.get('totnkvarh', None),
        timestamp = popms_data.get('timestamp', None),

    )

    logger.info(f"mongo_db = TemporaryPOPMSA006, topic = {topic} created {temp_popmsa006_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryPOPMSA006------------------------------!>')

    today_popmsa006_mongo = TodayPOPMSA006.objects.create(
        # _id = mongo_models.ObjectIdField(),
        created_time = utc_time.astimezone(dhaka_tz),
        topic = topic,
        dev_ID = popms_data.get('dev_ID', None),
        ac_temp_1 = popms_data.get('ac_temp_1', None),
        ac_temp_2 = popms_data.get('ac_temp_2', None),
        env_temp_1 = popms_data.get('env_temp_1', None),
        env_hum_1 = popms_data.get('env_hum_1', None),
        env_dp_1 = popms_data.get('env_dp_1', None),
        env_temp_2 = popms_data.get('env_temp_2', None),
        env_hum_2 = popms_data.get('env_hum_2', None),
        env_dp_2 = popms_data.get('env_dp_2', None),
        door_state_1 = popms_data.get('door_state_1', None),
        door_state_2 = popms_data.get('door_state_2', None),
        smoke_state = popms_data.get('smoke_state', None),
        ua = popms_data.get('ua', None),
        ub = popms_data.get('ub', None),
        uc = popms_data.get('uc', None),
        avln = popms_data.get('avln', None),
        uab = popms_data.get('uab', None),
        ubc = popms_data.get('ubc', None),
        uca = popms_data.get('uca', None),
        avll = popms_data.get('avll', None),
        ia = popms_data.get('ia', None),
        ib = popms_data.get('ib', None),
        ic = popms_data.get('ic', None),
        avc = popms_data.get('avc', None),
        pa = popms_data.get('pa', None),
        pb = popms_data.get('pb', None),
        pc = popms_data.get('pc', None),
        sa = popms_data.get('sa', None),
        sb = popms_data.get('sb', None),
        sc = popms_data.get('sc', None),
        qa = popms_data.get('qa', None),
        qb = popms_data.get('qb', None),
        qc = popms_data.get('qc', None),
        totkw = popms_data.get('totkw', None),
        totkva = popms_data.get('totkva', None),
        totkvar = popms_data.get('totkvar', None),
        pfa = popms_data.get('pfa', None),
        pfb = popms_data.get('pfb', None),
        pfc = popms_data.get('pfc', None),
        avpf = popms_data.get('avpf', None),
        f = popms_data.get('f', None),
        totnkwh = popms_data.get('totnkwh', None),
        totnkvah = popms_data.get('totnkvah', None),
        totnkvarh = popms_data.get('totnkvarh', None),
        timestamp = popms_data.get('timestamp', None),

    )

    logger.info(f"mongo_db = TodayPOPMSA006, topic = {topic} created {today_popmsa006_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayPOPMSA006------------------------------!>')



def date_wise_popmsa006_create(data, device_code, topic, flag):

    if "LAST_7_DAYS" in flag:
        last7days_popmsa006_mongo = Last7DaysPOPMSA006.objects.create(
            # _id = mongo_models.ObjectIdField(),
            # created_time = pytz.utc.localize(datetime.now()),
            topic = topic,
            dev_ID = device_code,
            ac_temp_1 = data.get('ac_temp_1', None),
            ac_temp_2 = data.get('ac_temp_2', None),
            env_temp_1 = data.get('env_temp_1', None),
            env_hum_1 = data.get('env_hum_1', None),
            env_dp_1 = data.get('env_dp_1', None),
            env_temp_2 = data.get('env_temp_2', None),
            env_hum_2 = data.get('env_hum_2', None),
            env_dp_2 = data.get('env_dp_2', None),
            door_state_1 = data.get('door_state_1', None),
            door_state_2 = data.get('door_state_2', None),
            smoke_state = data.get('smoke_state', None),
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            avln = data.get('avln', None),
            uab = data.get('uab', None),
            ubc = data.get('ubc', None),
            uca = data.get('uca', None),
            avll = data.get('avll', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            avc = data.get('avc', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            sa = data.get('sa', None),
            sb = data.get('sb', None),
            sc = data.get('sc', None),
            qa = data.get('qa', None),
            qb = data.get('qb', None),
            qc = data.get('qc', None),
            totkw = data.get('totkw', None),
            totkva = data.get('totkva', None),
            totkvar = data.get('totkvar', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            avpf = data.get('avpf', None),
            f = data.get('f', None),
            totnkwh = data.get('totnkwh', None),
            totnkvah = data.get('totnkvah', None),
            totnkvarh = data.get('totnkvarh', None),
            timestamp = data.get('timestamp', None),

        )

        logger.info(f"mongo_db = Last7DaysPOPMSA006, topic = {topic} created {last7days_popmsa006_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysPOPMSA006------------------------------!>')


    if "LAST_30_DAYS" in flag:
        last30days_popmsa006_mongo = Last30DaysPOPMSA006.objects.create(
            # _id = mongo_models.ObjectIdField(),
            # created_time = pytz.utc.localize(datetime.now()),
            topic = topic,
            dev_ID = device_code,
            ac_temp_1 = data.get('ac_temp_1', None),
            ac_temp_2 = data.get('ac_temp_2', None),
            env_temp_1 = data.get('env_temp_1', None),
            env_hum_1 = data.get('env_hum_1', None),
            env_dp_1 = data.get('env_dp_1', None),
            env_temp_2 = data.get('env_temp_2', None),
            env_hum_2 = data.get('env_hum_2', None),
            env_dp_2 = data.get('env_dp_2', None),
            door_state_1 = data.get('door_state_1', None),
            door_state_2 = data.get('door_state_2', None),
            smoke_state = data.get('smoke_state', None),
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            avln = data.get('avln', None),
            uab = data.get('uab', None),
            ubc = data.get('ubc', None),
            uca = data.get('uca', None),
            avll = data.get('avll', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            avc = data.get('avc', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            sa = data.get('sa', None),
            sb = data.get('sb', None),
            sc = data.get('sc', None),
            qa = data.get('qa', None),
            qb = data.get('qb', None),
            qc = data.get('qc', None),
            totkw = data.get('totkw', None),
            totkva = data.get('totkva', None),
            totkvar = data.get('totkvar', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            avpf = data.get('avpf', None),
            f = data.get('f', None),
            totnkwh = data.get('totnkwh', None),
            totnkvah = data.get('totnkvah', None),
            totnkvarh = data.get('totnkvarh', None),
            timestamp = data.get('timestamp', None),

        )

        logger.info(f"mongo_db = Last30DaysPOPMSA006, topic = {topic} created {last30days_popmsa006_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysPOPMSA006------------------------------!>')

    
    if "THIS_YEAR" in flag:
        thisyear_popmsa006_mongo = ThisYearPOPMSA006.objects.create(
            # _id = mongo_models.ObjectIdField(),
            # created_time = pytz.utc.localize(datetime.now()),
            topic = topic,
            dev_ID = device_code,
            ac_temp_1 = data.get('ac_temp_1', None),
            ac_temp_2 = data.get('ac_temp_2', None),
            env_temp_1 = data.get('env_temp_1', None),
            env_hum_1 = data.get('env_hum_1', None),
            env_dp_1 = data.get('env_dp_1', None),
            env_temp_2 = data.get('env_temp_2', None),
            env_hum_2 = data.get('env_hum_2', None),
            env_dp_2 = data.get('env_dp_2', None),
            door_state_1 = data.get('door_state_1', None),
            door_state_2 = data.get('door_state_2', None),
            smoke_state = data.get('smoke_state', None),
            ua = data.get('ua', None),
            ub = data.get('ub', None),
            uc = data.get('uc', None),
            avln = data.get('avln', None),
            uab = data.get('uab', None),
            ubc = data.get('ubc', None),
            uca = data.get('uca', None),
            avll = data.get('avll', None),
            ia = data.get('ia', None),
            ib = data.get('ib', None),
            ic = data.get('ic', None),
            avc = data.get('avc', None),
            pa = data.get('pa', None),
            pb = data.get('pb', None),
            pc = data.get('pc', None),
            sa = data.get('sa', None),
            sb = data.get('sb', None),
            sc = data.get('sc', None),
            qa = data.get('qa', None),
            qb = data.get('qb', None),
            qc = data.get('qc', None),
            totkw = data.get('totkw', None),
            totkva = data.get('totkva', None),
            totkvar = data.get('totkvar', None),
            pfa = data.get('pfa', None),
            pfb = data.get('pfb', None),
            pfc = data.get('pfc', None),
            avpf = data.get('avpf', None),
            f = data.get('f', None),
            totnkwh = data.get('totnkwh', None),
            totnkvah = data.get('totnkvah', None),
            totnkvarh = data.get('totnkvarh', None),
            timestamp = data.get('timestamp', None),

        )

        number_of_rows = ThisYearPOPMSA006.objects.all().count()
    
        if(number_of_rows > 365):
            objects_to_delete = ThisYearPOPMSA006.objects.filter(dev_ID=device_code, topic=topic).order_by('-created_date')[365:number_of_rows]
            for obj in objects_to_delete:
                obj.delete()

        logger.info(f"mongo_db = ThisYearPOPMSA006, topic = {topic} created {thisyear_popmsa006_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearPOPMSA006------------------------------!>')

