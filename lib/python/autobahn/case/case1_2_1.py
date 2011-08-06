###############################################################################
##
##  Copyright 2011 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from case import Case

class Case1_2_1(Case):

   ID = "1.2.1"

   DESCRIPTION = """Send binary message with payload 0."""

   EXPECTATION = """Receive echo'ed binary message (with empty payload)."""

   def onOpen(self):
      payload = ""
      self.expected = [("message", payload, True), ("failedByMe", True)]
      self.p.sendFrame(opcode = 2, payload = payload)
      self.p.killAfter(1)