class NonRelRouter:
    """
    A router to control if database should use
    primary database or non-relational one.
    """
    nonrel_models = {
        'yearlytuyaenergymetermongo', 
        'dailytuyaenergymetermongo', 
        'hourlytuyaenergymetermongo', 
        'tuyaenergymetermongo', 
        'temptuyaenergymetermongo', 
        'todaytuyaenergymetermongo', 
        'tempairqualitymongo', 
        'airqualitymongo', 
        'todayairqualitymongo', 
        'thisweekairqualitymongo', 
        'thismonthairqualitymongo', 
        'thisyearairqualitymongo',
        'rtmodelcpm',
        'todayrtmodelcpm',
        'thisweekrtmodelcpm',
        'thismonthrtmodelcpm',
        'thisyearrtmodelcpm',
        'daydatamodelcpm',
        'enynowdatamodelcpm',
        'enyfrzdatamodelcpm',
        'temporaryrtmodelcpm',
        'thermohygrometermongomodel',
        'tempthermohygrometermongomodel',
        'todaythermohygrometermongomodel',
        'thisweekthermohygrometermongomodel',
        'thismonththermohygrometermongomodel',
        'thisyearthermohygrometermongomodel',
        'temporaryhourlyrtmodelcpm',
        'temporary6hourrtmodelcpm',

        'popmsa006',
        'todaypopmsa006',
        'temporarypopmsa006',
        'last7dayspopmsa006',
        'last30dayspopmsa006',
        'thisyearpopmsa006',

        'popmsa006externalinfo',
        'todaypopmsa006externalinfo',
        'temporarypopmsa006externalinfo',
        'last7dayspopmsa006externalinfo',
        'last30dayspopmsa006externalinfo',
        'thisyearpopmsa006externalinfo',

        'thisweekpopmsa006',
        'thismonthpopmsa006',
        'latestpopmsa006',
        'last6hrpopmsa006',
        'hourlytemporarypopmsa006externalinfo',
    }

    def db_for_read(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def db_for_write(self, model, **_hints):
        if model._meta.model_name in self.nonrel_models:
            return 'nonrel'
        return 'default'

    def allow_migrate(self, _db, _app_label, model_name=None, **_hints):
        if _db == 'nonrel' or model_name in self.nonrel_models:
            return False
        return True
