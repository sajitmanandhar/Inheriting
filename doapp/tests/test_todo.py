# class TestTodo(TransactionCase):
from odoo.exceptions import AccessError
    def setUp(self,*args,**kwargs):
        result = super(TestTodo,self).setUp(*args,\
            **kwargs)
        user_demo = self.env.ref('base.user_demo')  
        self.env = self.env(user=user_demo)
        return result  