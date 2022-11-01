# Paramters
DEVICE_ID = "device_id"
DEVICE_NAME = "device_name"
DEVICE_MODEL = "device_model"
DISCOVERY_TOPIC = "discovery_topic"
DOOR_SENSOR_AVAILABLE = "door_sensor_available"
KEYPAD_AVAILABLE = "keypad_available"

DEFAULT_DISCOVERY_TOPIC = "homeassistant"

# Topics
TOPIC_BASE = "nuki"
TOPIC_STATE = "state"
TOPIC_LOCK_ACTION = "lockAction"
TOPIC_CONNECTED = "connected"
TOPIC_BATTERY_CRITICAL = "batteryCritical"
TOPIC_BATTERY_CHARGE_STATE = "batteryChargeState"
TOPIC_BATTERY_CHARGING = "batteryCharging"
TOPIC_DOOR_SENSOR_STATE = "doorsensorState"
TOPIC_DOOR_SENSOR_BATTERY_CIRITCAL = "doorsensorBatteryCritical"
TOPIC_KEYPAD_BATTERY_CRITICAL = "keypadBatteryCritical"

# Lock states
STATE_UNCALIBRATED = 0
STATE_LOCKED = 1
STATE_UNLOCKING = 2
STATE_UNLOCKED = 3
STATE_LOCKING = 4
STATE_UNLATCHED = 5
STATE_UNLOCKED_LOCKNGO = 6
STATE_UNLATCHING = 7
STATE_MOTOR_BLOCKED = 254
STATE_UNDEFINED = 255

# Lock actions
ACTION_UNLOCK = 1
ACTION_LOCK = 2
ACTION_UNLATCH = 3
ACTION_LOCKNGO = 4
ACTION_LOCKNGO_UNLATCH = 5
ACTION_FULL_LOCK = 6
ACTION_FOB = 80
ACTION_BUTTON = 90

# Door sensor states
DOOR_STATE_DEACTIVATED = 1
DOOR_STATE_DOOR_CLOSED = 2
DOOR_STATE_DOOR_OPENED = 3
DOOR_STATE_DOOR_STATE_UNKNOWN = 4
DOOR_STATE_CALIBRATING = 5
DOOR_STATE_UNCALIBRATED = 16
DOOR_STATE_TAMPERED = 240
DOOR_STATE_UNKNOWN = 255


def get_error_message(parameter):
  return "Parameter " + parameter + " is required!"


def get_object_id(name):  
  return name.replace(" ", "_").replace("-", "_").lower()


def to_json(dictonary):
  return '{}'.format(dictonary).replace("\'", "\"").replace("\"\"", "\'")


def get_discovery_topic(discovery_topic, component, node_id, name):
  return discovery_topic + "/" + component + "/" + node_id + "/" + get_object_id(name) + "/config"


def get_topic(device_id, topic):
  return TOPIC_BASE + "/" + device_id + "/" + topic


def get_availability(device_id):
  return [
    {
      'topic': get_topic(device_id, TOPIC_CONNECTED),
      'payload_available': 'true',
      'payload_not_available': 'false'
    }
  ]


def get_device(device_id, device_name, device_model):
  return {
    'identifiers': [
        device_id
    ],
    'manufacturer': 'Nuki',
    'name': device_name,
    'model': device_model
  }


def get_lock_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'command_topic': get_topic(device_id, TOPIC_LOCK_ACTION),
    'payload_lock': str(ACTION_LOCK),
    'payload_unlock': str(ACTION_UNLOCK),
    'payload_open': str(ACTION_UNLATCH),
    'state_topic': get_topic(device_id, TOPIC_STATE),
    'state_locked': str(STATE_LOCKED),
    'state_unlocked': str(STATE_UNLOCKED),
    'state_opening': str(STATE_UNLATCHING),
    'state_open': str(STATE_UNLATCHED),
    'value_template': '{% if value == \'\'' + str(STATE_UNLOCKED_LOCKNGO) + '\'\'%}' + str(STATE_UNLOCKED) + '{% else %}{{value}}{% endif %}'
  })


def get_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'battery',
    'entity_category': 'diagnostic',
    'state_topic': get_topic(device_id, TOPIC_BATTERY_CRITICAL),
    'payload_off': 'false',
    'payload_on': 'true'
  })


def get_battery_charge_state_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'battery',
    'entity_category': 'diagnostic',
    'state_topic': get_topic(device_id, TOPIC_BATTERY_CHARGE_STATE),
    'state_class': 'measurement',
    'unit_of_measurement': '%'
  })


def get_battery_charging_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'battery_charging',
    'entity_category': 'diagnostic',
    'state_topic': get_topic(device_id, TOPIC_BATTERY_CHARGING),
    'payload_off': 'false',
    'payload_on': 'true'
  })


def get_door_sensor_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'door',
    'payload_off': str(DOOR_STATE_DOOR_CLOSED),
    'payload_on': str(DOOR_STATE_DOOR_OPENED),
    'state_topic': get_topic(device_id, TOPIC_DOOR_SENSOR_STATE),
  })


def get_door_sensor_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'battery',
    'entity_category': 'diagnostic',
    'state_topic': get_topic(device_id, TOPIC_DOOR_SENSOR_BATTERY_CIRITCAL),
    'payload_off': 'false',
    'payload_on': 'true'
  })


def get_keypad_battery_critical_payload(device_id, device_name, device_model, name):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'device_class': 'battery',
    'entity_category': 'diagnostic',
    'state_topic': get_topic(device_id, TOPIC_KEYPAD_BATTERY_CRITICAL),
    'payload_off': 'false',
    'payload_on': 'true'
  })


def get_button_payload(device_id, device_name, device_model, name, action):
  return to_json({
    'availability': get_availability(device_id),
    'device': get_device(device_id, device_name, device_model),
    'name': name,
    'unique_id': get_object_id(name),
    'command_topic': get_topic(device_id, TOPIC_LOCK_ACTION),
    'payload_press': str(action)
  })


def publish(hass, topic, payload):
  data = {
    "topic": topic,
    "payload": payload,
    "retain": 'true'
  }

  hass.services.call("mqtt", "publish", data)


def main(hass, data):
  device_id = data.get(DEVICE_ID)
  device_name = data.get(DEVICE_NAME)
  device_model = data.get(DEVICE_MODEL)
  discovery_topic = data.get(DISCOVERY_TOPIC)
  door_sensor_available = data.get(DOOR_SENSOR_AVAILABLE)
  keypad_available = data.get(KEYPAD_AVAILABLE)

  if device_id == None or device_id == "":
    logger.error(get_error_message(device_id))
    return
  
  if device_name == None or device_name == "":
    logger.error(get_error_message(device_id))
    return

  if device_model == None or device_model == "":
    logger.error(get_error_message(device_id))
    return

  if discovery_topic == None or discovery_topic == "":
    logger.info("Parameter " + str(discovery_topic) + " was not passed. Default topic (homeassistant) is used.")
    discovery_topic = DEFAULT_DISCOVERY_TOPIC

  if door_sensor_available == None:
    door_sensor_available = False
  
  if keypad_available == None:
    keypad_available = False

  # Lock
  name = device_name
  publish(hass, get_discovery_topic(discovery_topic, "lock", device_id, name),
    get_lock_payload(device_id, device_name, device_model, name))

  # Battery critical
  name = device_name + " Battery Critical"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), 
    get_battery_critical_payload(device_id, device_name, device_model, name))

  # Battery charge state
  name = device_name + " Battery"
  publish(hass, get_discovery_topic(discovery_topic, "sensor", device_id, name),
    get_battery_charge_state_payload(device_id, device_name, device_model, name))

  # Battery charging
  name = device_name + " Battery Charging"
  publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name),
    get_battery_charging_payload(device_id, device_name, device_model, name))

  if door_sensor_available:
    # Door sensor
    name = device_name + " Door Sensor"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name),
      get_door_sensor_payload(device_id, device_name, device_model, name))

    # Door sensor battery critical
    name = device_name + " Door Sensor Battery Critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), 
      get_door_sensor_battery_critical_payload(device_id, device_name, device_model, name))

  if keypad_available:
    # Keypad battery critical
    name = device_name + " Keypad Battery Critical"
    publish(hass, get_discovery_topic(discovery_topic, "binary_sensor", device_id, name), 
      get_keypad_battery_critical_payload(device_id, device_name, device_model, name))

  # Unlatch button
  name = device_name + " Unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name),
    get_button_payload(device_id, device_name, device_model, name, ACTION_UNLATCH))

  # Lock'n'Go button
  name = device_name + " Lock-n-Go"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name),
    get_button_payload(device_id, device_name, device_model, name, ACTION_LOCKNGO))

  # Lock'n'Go with unlatch button
  name = device_name + " Lock-n-Go With Unlatch"
  publish(hass, get_discovery_topic(discovery_topic, "button", device_id, name),
    get_button_payload(device_id, device_name, device_model, name, ACTION_LOCKNGO_UNLATCH))


main(hass, data)
