from events import event_actions, event_subjects
from events.event import Attribute, Event

NOTEBOOK_STARTED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.STARTED)
NOTEBOOK_STARTED_TRIGGERED = '{}.{}.{}'.format(event_subjects.NOTEBOOK,
                                               event_actions.STARTED,
                                               event_subjects.TRIGGER)
NOTEBOOK_STOPPED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.STOPPED)
NOTEBOOK_STOPPED_TRIGGERED = '{}.{}.{}'.format(event_subjects.NOTEBOOK,
                                               event_actions.STOPPED,
                                               event_subjects.TRIGGER)
NOTEBOOK_CLEANED_TRIGGERED = '{}.{}.{}'.format(event_subjects.NOTEBOOK,
                                               event_actions.CLEANED,
                                               event_subjects.TRIGGER)
NOTEBOOK_VIEWED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.VIEWED)
NOTEBOOK_UPDATED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.UPDATED)
NOTEBOOK_DELETED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.DELETED)
NOTEBOOK_DELETED_TRIGGERED = '{}.{}.{}'.format(event_subjects.NOTEBOOK,
                                               event_actions.DELETED,
                                               event_subjects.TRIGGER)
NOTEBOOK_ARCHIVED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.ARCHIVED)
NOTEBOOK_RESTORED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.RESTORED)
NOTEBOOK_BOOKMARKED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.BOOKMARKED)
NOTEBOOK_UNBOOKMARKED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.UNBOOKMARKED)
NOTEBOOK_NEW_STATUS = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.NEW_STATUS)
NOTEBOOK_FAILED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.FAILED)
NOTEBOOK_SUCCEEDED = '{}.{}'.format(event_subjects.NOTEBOOK, event_actions.SUCCEEDED)
NOTEBOOK_STATUSES_VIEWED = '{}.{}'.format(event_subjects.NOTEBOOK,
                                          event_actions.STATUSES_VIEWED)

EVENTS = {
    NOTEBOOK_STARTED,
    NOTEBOOK_STARTED_TRIGGERED,
    NOTEBOOK_STOPPED,
    NOTEBOOK_STOPPED_TRIGGERED,
    NOTEBOOK_CLEANED_TRIGGERED,
    NOTEBOOK_VIEWED,
    NOTEBOOK_UPDATED,
    NOTEBOOK_DELETED,
    NOTEBOOK_DELETED_TRIGGERED,
    NOTEBOOK_ARCHIVED,
    NOTEBOOK_RESTORED,
    NOTEBOOK_BOOKMARKED,
    NOTEBOOK_UNBOOKMARKED,
    NOTEBOOK_NEW_STATUS,
    NOTEBOOK_FAILED,
    NOTEBOOK_SUCCEEDED,
    NOTEBOOK_STATUSES_VIEWED,
}


class NotebookStartedEvent(Event):
    event_type = NOTEBOOK_STARTED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookStartedTriggeredEvent(Event):
    event_type = NOTEBOOK_STARTED_TRIGGERED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookSoppedEvent(Event):
    event_type = NOTEBOOK_STOPPED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
    )


class NotebookCleanedTriggeredEvent(Event):
    event_type = NOTEBOOK_CLEANED_TRIGGERED
    attributes = (
        Attribute('id'),
    )


class NotebookSoppedTriggeredEvent(Event):
    event_type = NOTEBOOK_STOPPED_TRIGGERED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('target'),  # project, experiment_group, experiment
        Attribute('last_status'),
    )


class NotebookViewedEvent(Event):
    event_type = NOTEBOOK_VIEWED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
    )


class NotebookNewStatusEvent(Event):
    event_type = NOTEBOOK_NEW_STATUS
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookSucceededEvent(Event):
    event_type = NOTEBOOK_SUCCEEDED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookFailedEvent(Event):
    event_type = NOTEBOOK_FAILED
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('last_status'),
        Attribute('previous_status', is_required=False),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookStatusesViewedEvent(Event):
    event_type = NOTEBOOK_STATUSES_VIEWED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('user.id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookUpdatedEvent(Event):
    event_type = NOTEBOOK_UPDATED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
    )


class NotebookDeletedTriggeredEvent(Event):
    event_type = NOTEBOOK_DELETED_TRIGGERED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
    )


class NotebookDeletedEvent(Event):
    event_type = NOTEBOOK_DELETED
    attributes = (
        Attribute('id'),
    )


class NotebookBookmarkedEvent(Event):
    event_type = NOTEBOOK_BOOKMARKED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookUnBookmarkedEvent(Event):
    event_type = NOTEBOOK_UNBOOKMARKED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
        Attribute('target'),  # project, experiment_group, experiment
    )


class NotebookArchivedEvent(Event):
    event_type = NOTEBOOK_ARCHIVED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
    )


class NotebookRestoredEvent(Event):
    event_type = NOTEBOOK_RESTORED
    actor = True
    attributes = (
        Attribute('id'),
        Attribute('user.id'),
        Attribute('project.id'),
        Attribute('project.user.id'),
        Attribute('last_status'),
    )
