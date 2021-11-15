import typing
from formify.layout import Col
from PySide6 import QtWidgets, QtCore


class Segment(QtWidgets.QFrame):
	def __init__(self, layout_or_control, *args):
		super().__init__()
		self.setContentsMargins(7, 7, 7, 7)

		if isinstance(layout_or_control, QtWidgets.QLayout) and len(args) == 0:
			self.setLayout(layout_or_control)
		else:
			self.setLayout(Col(
				layout_or_control,
				*args
			))


class SegmentAlt(Segment):
	pass


class SegmentRed(Segment):
	pass


class SegmentYellow(Segment):
	pass


class SegmentGreen(Segment):
	pass


class SegmentBlue(Segment):
	pass


class SegmentPurple(Segment):
	pass


class SegmentSidebar(Segment):
	pass
