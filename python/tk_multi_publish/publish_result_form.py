"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""

import tank
from tank.platform.qt import QtCore, QtGui
 
class PublishResultForm(QtGui.QWidget):
    """
    Implementation of the main publish UI
    """
    
    close = QtCore.Signal()
    
    def __init__(self, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
    
        self._status = True
        self._errors = []
    
        # set up the UI
        from .ui.publish_result_form import Ui_PublishResultForm
        self._ui = Ui_PublishResultForm() 
        self._ui.setupUi(self)
        
        self._ui.close_btn.clicked.connect(self._on_close)
        
        self._update_ui()
        
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
        self._update_ui()
    
    @property
    def errors(self):
        return self._errors
    @errors.setter
    def errors(self, value):
        self._errors = value
        self._update_ui()
        
    def _on_close(self):
        self.close.emit()
        
    def _update_ui(self):
        
        self._ui.status_icon.setPixmap(QtGui.QPixmap([":/res/failure.png", ":/res/success.png"][self._status]))
        self._ui.status_title.setText(["Failure!", "Success"][self._status])
        self._ui.status_details.setText("\n".join(self._errors))
        
        