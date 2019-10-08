
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DIGIT DIVIDE EQUALS GLOBAL_VARIABLE_ID LOCAL_VARIABLE_ID LPAR MINUS MODULE NSW NUMBER OPERATION PLUS RPAR SEMICOLON TIMES VARTYPEinstr0 : instr1\n              | func instr1 : operand1 EQUALS funcfunc : OPERATION operand0\n            | OPERATION operand1operand0 : operand3 COMMA operand3\n                | operand4 COMMA operand3\n                | operand3 COMMA operand4operand1 : operand3\n                | operand4 operand3 : VARTYPE LOCAL_VARIABLE_ID\n                | VARTYPE NUMBER operand4 : VARTYPE\n                | LOCAL_VARIABLE_ID\n                | NUMBER '
    
_lr_action_items = {'EQUALS':([1,2,3,4,7,10,12,13,],[-10,11,-9,-15,-13,-14,-11,-12,]),'NUMBER':([0,7,9,20,22,],[4,13,4,4,13,]),'COMMA':([4,7,10,12,13,14,17,],[-15,-13,-14,-11,-12,19,20,]),'VARTYPE':([0,9,19,20,],[7,7,22,7,]),'OPERATION':([0,11,],[9,9,]),'LOCAL_VARIABLE_ID':([0,7,9,20,22,],[10,12,10,10,12,]),'$end':([4,5,6,7,8,10,12,13,14,15,16,17,18,21,23,24,],[-15,0,-1,-13,-2,-14,-11,-12,-10,-5,-4,-9,-3,-7,-8,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'operand4':([0,9,20,],[1,14,23,]),'operand1':([0,9,],[2,15,]),'operand0':([9,],[16,]),'operand3':([0,9,19,20,],[3,17,21,24,]),'instr0':([0,],[5,]),'instr1':([0,],[6,]),'func':([0,11,],[8,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instr0","S'",1,None,None,None),
  ('instr0 -> instr1','instr0',1,'p_instr0','compiler.py',135),
  ('instr0 -> func','instr0',1,'p_instr0','compiler.py',136),
  ('instr1 -> operand1 EQUALS func','instr1',3,'p_instr1','compiler.py',139),
  ('func -> OPERATION operand0','func',2,'p_func','compiler.py',142),
  ('func -> OPERATION operand1','func',2,'p_func','compiler.py',143),
  ('operand0 -> operand3 COMMA operand3','operand0',3,'p_operand0','compiler.py',147),
  ('operand0 -> operand4 COMMA operand3','operand0',3,'p_operand0','compiler.py',148),
  ('operand0 -> operand3 COMMA operand4','operand0',3,'p_operand0','compiler.py',149),
  ('operand1 -> operand3','operand1',1,'p_operand1','compiler.py',155),
  ('operand1 -> operand4','operand1',1,'p_operand1','compiler.py',156),
  ('operand3 -> VARTYPE LOCAL_VARIABLE_ID','operand3',2,'p_operand3','compiler.py',161),
  ('operand3 -> VARTYPE NUMBER','operand3',2,'p_operand3','compiler.py',162),
  ('operand4 -> VARTYPE','operand4',1,'p_operand4','compiler.py',166),
  ('operand4 -> LOCAL_VARIABLE_ID','operand4',1,'p_operand4','compiler.py',167),
  ('operand4 -> NUMBER','operand4',1,'p_operand4','compiler.py',168),
]
