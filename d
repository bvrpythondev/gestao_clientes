Help on ManyRelatedManager in module django.db.models.fields.related_descriptors object:

class MMaannyyRReellaatteeddMMaannaaggeerr(django.contrib.auth.models.GroupManager)
 |  The manager for the auth's Group model.
 |  
 |  Method resolution order:
 |      ManyRelatedManager
 |      django.contrib.auth.models.GroupManager
 |      django.db.models.manager.Manager
 |      django.db.models.manager.BaseManagerFromQuerySet
 |      django.db.models.manager.BaseManager
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  ____ccaallll____(self, *, manager)
 |  
 |  ____iinniitt____(self, instance=None)
 |  
 |  aadddd(self, *objs, through_defaults=None)
 |  
 |  cclleeaarr(self)
 |  
 |  ccrreeaattee(self, *, through_defaults=None, **kwargs)
 |  
 |  ggeett__oorr__ccrreeaattee(self, *, through_defaults=None, **kwargs)
 |  
 |  ggeett__pprreeffeettcchh__qquueerryysseett(self, instances, queryset=None)
 |  
 |  ggeett__qquueerryysseett(self)
 |  
 |  rreemmoovvee(self, *objs)
 |  
 |  sseett(self, objs, *, clear=False, through_defaults=None)
 |  
 |  uuppddaattee__oorr__ccrreeaattee(self, *, through_defaults=None, **kwargs)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  ddoo__nnoott__ccaallll__iinn__tteemmppllaatteess = True
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from django.contrib.auth.models.GroupManager:
 |  
 |  ggeett__bbyy__nnaattuurraall__kkeeyy(self, name)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from django.contrib.auth.models.GroupManager:
 |  
 |  ____sslloottnnaammeess____ = []
 |  
 |  uussee__iinn__mmiiggrraattiioonnss = True
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from django.db.models.manager.BaseManagerFromQuerySet:
 |  
 |  aaggggrreeggaattee(self, *args, **kwargs)
 |      Return a dictionary containing the calculations (aggregation)
 |      over the current queryset.
 |      
 |      If args is present the expression is passed as a kwarg using
 |      the Aggregate object's default alias.
 |  
 |  aannnnoottaattee(self, *args, **kwargs)
 |      Return a query set in which the returned objects have been annotated
 |      with extra data or aggregations.
 |  
 |  bbuullkk__ccrreeaattee(self, *args, **kwargs)
 |      Insert each of the instances into the database. Do *not* call
 |      save() on each of the instances, do not send any pre/post_save
 |      signals, and do not set the primary key attribute if it is an
 |      autoincrement field (except if features.can_return_ids_from_bulk_insert=True).
 |      Multi-table models are not supported.
 |  
 |  bbuullkk__uuppddaattee(self, *args, **kwargs)
 |      Update the given fields in each of the given objects in the database.
 |  
 |  ccoommpplleexx__ffiilltteerr(self, *args, **kwargs)
 |      Return a new QuerySet instance with filter_obj added to the filters.
 |      
 |      filter_obj can be a Q object or a dictionary of keyword lookup
 |      arguments.
 |      
 |      This exists to support framework features such as 'limit_choices_to',
 |      and usually it will be more natural to use other methods.
 |  
 |  ccoouunntt(self, *args, **kwargs)
 |      Perform a SELECT COUNT() and return the number of records as an
 |      integer.
 |      
 |      If the QuerySet is already fully cached, return the length of the
 |      cached results set to avoid multiple SELECT COUNT(*) calls.
 |  
 |  ddaatteess(self, *args, **kwargs)
 |      Return a list of date objects representing all available dates for
 |      the given field_name, scoped to 'kind'.
 |  
 |  ddaatteettiimmeess(self, *args, **kwargs)
 |      Return a list of datetime objects representing all available
 |      datetimes for the given field_name, scoped to 'kind'.
 |  
 |  ddeeffeerr(self, *args, **kwargs)
 |      Defer the loading of data for certain fields until they are accessed.
 |      Add the set of deferred fields to any existing set of deferred fields.
 |      The only exception to this is if None is passed in as the only
 |      parameter, in which case removal all deferrals.
 |  
 |  ddiiffffeerreennccee(self, *args, **kwargs)
 |  
 |  ddiissttiinncctt(self, *args, **kwargs)
 |      Return a new QuerySet instance that will select only distinct results.
 |  
 |  eeaarrlliieesstt(self, *args, **kwargs)
 |  
 |  eexxcclluuddee(self, *args, **kwargs)
 |      Return a new QuerySet instance with NOT (args) ANDed to the existing
 |      set.
 |  
 |  eexxiissttss(self, *args, **kwargs)
 |  
 |  eexxppllaaiinn(self, *args, **kwargs)
 |  
 |  eexxttrraa(self, *args, **kwargs)
 |      Add extra SQL fragments to the query.
 |  
 |  ffiilltteerr(self, *args, **kwargs)
 |      Return a new QuerySet instance with the args ANDed to the existing
 |      set.
 |  
 |  ffiirrsstt(self, *args, **kwargs)
 |      Return the first object of a query or None if no match is found.
 |  
 |  ggeett(self, *args, **kwargs)
 |      Perform the query and return a single object matching the given
 |      keyword arguments.
 |  
 |  iinn__bbuullkk(self, *args, **kwargs)
 |      Return a dictionary mapping each of the given IDs to the object with
 |      that ID. If `id_list` isn't provided, evaluate the entire QuerySet.
 |  
 |  iinntteerrsseeccttiioonn(self, *args, **kwargs)
 |  
 |  iitteerraattoorr(self, *args, **kwargs)
 |      An iterator over the results from applying this QuerySet to the
 |      database.
 |  
 |  llaasstt(self, *args, **kwargs)
 |      Return the last object of a query or None if no match is found.
 |  
 |  llaatteesstt(self, *args, **kwargs)
 |  
 |  nnoonnee(self, *args, **kwargs)
 |      Return an empty QuerySet.
 |  
 |  oonnllyy(self, *args, **kwargs)
 |      Essentially, the opposite of defer(). Only the fields passed into this
 |      method and that are not already specified as deferred are loaded
 |      immediately when the queryset is evaluated.
 |  
 |  oorrddeerr__bbyy(self, *args, **kwargs)
 |      Return a new QuerySet instance with the ordering changed.
 |  
 |  pprreeffeettcchh__rreellaatteedd(self, *args, **kwargs)
 |      Return a new QuerySet instance that will prefetch the specified
 |      Many-To-One and Many-To-Many related objects when the QuerySet is
 |      evaluated.
 |      
 |      When prefetch_related() is called more than once, append to the list of
 |      prefetch lookups. If prefetch_related(None) is called, clear the list.
 |  
 |  rraaww(self, *args, **kwargs)
 |  
 |  rreevveerrssee(self, *args, **kwargs)
 |      Reverse the ordering of the QuerySet.
 |  
 |  sseelleecctt__ffoorr__uuppddaattee(self, *args, **kwargs)
 |      Return a new QuerySet instance that will select objects with a
 |      FOR UPDATE lock.
 |  
 |  sseelleecctt__rreellaatteedd(self, *args, **kwargs)
 |      Return a new QuerySet instance that will select related objects.
 |      
 |      If fields are specified, they must be ForeignKey fields and only those
 |      related objects are included in the selection.
 |      
 |      If select_related(None) is called, clear the list.
 |  
 |  uunniioonn(self, *args, **kwargs)
 |  
 |  uuppddaattee(self, *args, **kwargs)
 |      Update all elements in the current QuerySet, setting all the given
 |      fields to the appropriate values.
 |  
 |  uussiinngg(self, *args, **kwargs)
 |      Select which database this QuerySet should execute against.
 |  
 |  vvaalluueess(self, *args, **kwargs)
 |  
 |  vvaalluueess__lliisstt(self, *args, **kwargs)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from django.db.models.manager.BaseManager:
 |  
 |  ____eeqq____(self, other)
 |      Return self==value.
 |  
 |  ____hhaasshh____(self)
 |      Return hash(self).
 |  
 |  ____ssttrr____(self)
 |      Return "app_label.model_label.manager_name".
 |  
 |  aallll(self)
 |  
 |  cchheecckk(self, **kwargs)
 |  
 |  ccoonnttrriibbuuttee__ttoo__ccllaassss(self, model, name)
 |  
 |  ddbb__mmaannaaggeerr(self, using=None, hints=None)
 |  
 |  ddeeccoonnssttrruucctt(self)
 |      Return a 5-tuple of the form (as_manager (True), manager_class,
 |      queryset_class, args, kwargs).
 |      
 |      Raise a ValueError if the manager is dynamically generated.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from django.db.models.manager.BaseManager:
 |  
 |  ffrroomm__qquueerryysseett(queryset_class, class_name=None) from builtins.type
 |  
 |  ----------------------------------------------------------------------
 |  Static methods inherited from django.db.models.manager.BaseManager:
 |  
 |  ____nneeww____(cls, *args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from django.db.models.manager.BaseManager:
 |  
 |  ____ddiicctt____
 |      dictionary for instance variables (if defined)
 |  
 |  ____wweeaakkrreeff____
 |      list of weak references to the object (if defined)
 |  
 |  ddbb
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from django.db.models.manager.BaseManager:
 |  
 |  aauuttoo__ccrreeaatteedd = False
 |  
 |  ccrreeaattiioonn__ccoouunntteerr = 23
