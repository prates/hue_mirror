#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, url


IS_URL_NAMESPACED = True


urlpatterns = patterns(
  'oozie.views.editor',

  url(r'^list_workflows/$', 'list_workflows', name='list_workflows'),
  url(r'^create_workflow/$', 'create_workflow', name='create_workflow'),
  url(r'^edit_workflow/(?P<workflow>\d+)$', 'edit_workflow', name='edit_workflow'),
  url(r'^delete_workflow/(?P<workflow>\d+)$', 'delete_workflow', name='delete_workflow'),
  url(r'^clone_workflow/(?P<workflow>\d+)$', 'clone_workflow', name='clone_workflow'),
  url(r'^submit_workflow/(?P<workflow>\d+)$', 'submit_workflow', name='submit_workflow'),

  url(r'^new_action/(?P<workflow>\d+)/(?P<node_type>\w+)/(?P<parent_action_id>\d+)$', 'new_action', name='new_action'),
  url(r'^edit_action/(?P<action>\d+)$', 'edit_action', name='edit_action'),
  url(r'^edit_workflow_fork/(?P<action>\d+)$', 'edit_workflow_fork', name='edit_workflow_fork'),
  url(r'^delete_action/(?P<action>\d+)$', 'delete_action', name='delete_action'),
  url(r'^clone_action/(?P<action>\d+)$', 'clone_action', name='clone_action'),
  url(r'^move_up_action/(?P<action>\d+)$', 'move_up_action', name='move_up_action'),
  url(r'^move_down_action/(?P<action>\d+)$', 'move_down_action', name='move_down_action'),

  url(r'^list_coordinator/$', 'list_workflows', name='list_coordinator', kwargs={'job_type': 'coordinators'}),
  url(r'^create_coordinator/(?P<workflow>[-\w]+)?$', 'create_coordinator', name='create_coordinator'),
  url(r'^edit_coordinator/(?P<coordinator>[-\w]+)$', 'edit_coordinator', name='edit_coordinator'),
  url(r'^create_coordinator_dataset/(?P<coordinator>[-\w]+)$', 'create_coordinator_dataset', name='create_coordinator_dataset'),
  url(r'^create_coordinator_data/(?P<coordinator>[-\w]+)/(?P<data_type>(input|output))$', 'create_coordinator_data', name='create_coordinator_data'),
  url(r'^submit_coordinator/(?P<coordinator>\d+)$', 'submit_coordinator', name='submit_coordinator'),

  url(r'^workflow_parameters/(?P<workflow>\d+)$', 'get_workflow_parameters', name='workflow_parameters'),
  url(r'^list_history$', 'list_history', name='list_history'),
  url(r'^list_history/(?P<record_id>[-\w]+)$', 'list_history_record', name='list_history_record'),
  url(r'^setup/$', 'setup', name='setup'),
)

urlpatterns += patterns(
  'oozie.views.dashboard',

  url(r'^$', 'list_oozie_workflows', name='index'),

  url(r'^list_oozie_workflows/$', 'list_oozie_workflows', name='list_oozie_workflows'),
  url(r'^list_oozie_coordinators/$', 'list_oozie_coordinators', name='list_oozie_coordinators'),
  url(r'^list_oozie_workflow/(?P<job_id>[-\w]+)/(?P<coordinator_job_id>[-\w]+)?$', 'list_oozie_workflow', name='list_oozie_workflow'),
  url(r'^list_oozie_coordinator/(?P<job_id>[-\w]+)$', 'list_oozie_coordinator', name='list_oozie_coordinator'),
  url(r'^list_oozie_coordinator_from_job/(?P<job_id>[-\w]+)$', 'list_oozie_coordinator_from_job', name='list_oozie_coordinator_from_job'),
  url(r'^list_oozie_workflow_action/(?P<action>[-\w@]+)$', 'list_oozie_workflow_action', name='list_oozie_workflow_action'),
  url(r'^manage_oozie_jobs/(?P<job_id>[-\w]+)/(?P<action>(start|suspend|resume|kill|rerun))$', 'manage_oozie_jobs', name='manage_oozie_jobs'),
)
