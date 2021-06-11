# _*_ coding: utf-8 _*_

from odoo import models, fields,api
class TodoTask(models.Model):
	@api.multi
	def do_toggle_done(self):
		for task in self:
			task.is_done = not task.is_done
		return True	
 
	 #should be api.model according to booklet but if new function
	               # then we should use multi function
	@api.multi 			   
	def do_clear_done(self):
		dones = self.search([('is_done', '=', True)])
		dones.write({'active' : False})
		return True		
	_name= 'todo.task'
	_description = 'DOapp Task'
	name = fields.Char('Name', required=True)
	is_done = fields.Boolean('IfDone?')
	active = fields.Boolean('Active?', default=True)
  
