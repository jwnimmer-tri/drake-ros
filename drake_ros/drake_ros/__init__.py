"""Python wrapper for drake_ros.core."""

from drake_ros._cc import *

from pydrake.common.value import AbstractValue
from pydrake.systems.framework import TriggerType

from rclpy.serialization import serialize_message
from rclpy.serialization import deserialize_message
from rclpy.type_support import check_for_type_support


class PySerializer(SerializerInterface):
    """
    A (de)serialization interface for Python ROS messages.
    """

    def __init__(self, message_type):
        SerializerInterface.__init__(self)
        check_for_type_support(message_type)
        self._message_type = message_type

    def GetTypeSupport(self):
        return self._message_type._TYPE_SUPPORT

    def CreateDefaultValue(self):
        return AbstractValue.Make(self._message_type())

    def Serialize(self, abstract_value):
        return serialize_message(abstract_value.get_value())

    def Deserialize(self, serialized_message, abstract_value):
        abstract_value.set_value(deserialize_message(
            serialized_message, self._message_type))


@staticmethod
def _make_ros_publisher_system(
    message_type, topic_name, qos, ros_interface,
    publish_triggers={
        TriggerType.kPerStep,
        TriggerType.kForced},
    publish_period=0.0
):
    return RosPublisherSystem(
        PySerializer(message_type),
        topic_name, qos, ros_interface,
        publish_triggers, publish_period)


RosPublisherSystem.Make = _make_ros_publisher_system


@staticmethod
def _make_ros_subscriber_system(
    message_type, topic_name, qos, ros_interface
):
    return RosSubscriberSystem(
        PySerializer(message_type),
        topic_name, qos, ros_interface)


RosSubscriberSystem.Make = _make_ros_subscriber_system


__all__ = [
    'DrakeRosInterface',
    'Isometry3ToRosPose',
    'Isometry3ToRosTransform',
    'PySerializer',
    'QuaternionToRosQuaternion',
    'RigidTransformToRosPose',
    'RigidTransformToRosTransform',
    'RosAccelToSpatialAcceleration',
    'RosAccelToVector6',
    'RosInterfaceSystem',
    'RosPointToVector3',
    'RosPoseToIsometry3',
    'RosPoseToRigidTransform',
    'RosPublisherSystem',
    'RosQuaternionToQuaternion',
    'RosQuaternionToRotationMatrix',
    'RosSubscriberSystem',
    'RosTransformToIsometry3',
    'RosTransformToRigidTransform',
    'RosTwistToSpatialVelocity',
    'RosTwistToVector6',
    'RosVector3ToVector3',
    'RosWrenchToSpatialForce',
    'RosWrenchToVector6',
    'RotationMatrixToRosQuaternion',
    'RvizVisualizer',
    'RvizVisualizerParams',
    'SceneTfBroadcasterParams',
    'SceneTfBroadcasterSystem',
    'SerializerInterface',
    'SpatialAccelerationToRosAccel',
    'SpatialForceToRosWrench',
    'SpatialVelocityToRosTwist',
    'Vector3ToRosPoint',
    'Vector3ToRosVector3',
    'Vector6ToRosAccel',
    'Vector6ToRosTwist',
    'Vector6ToRosWrench',
    'init',
    'shutdown',
]
