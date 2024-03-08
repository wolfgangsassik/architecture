.. _section-system-scope-and-context:

System Scope and Context
========================

.. container:: formalpara-title

   **Contents**

System scope and context - as the name suggests - delimits your system
(i.e. your scope) from all its communication partners (neighboring
systems and users, i.e. the context of your system). It thereby
specifies the external interfaces.

If necessary, differentiate the business context (domain specific inputs
and outputs) from the technical context (channels, protocols, hardware).

.. container:: formalpara-title

   **Motivation**

The domain interfaces and technical interfaces to communication partners
are among your system’s most critical aspects. Make sure that you
completely understand them.

.. container:: formalpara-title

   **Form**

Various options:

-  Context diagrams

-  Lists of communication partners and their interfaces.

See `Context and Scope <https://docs.arc42.org/section-3/>`__ in the
arc42 documentation.

.. _`_business_context`:

Business Context
----------------

.. container:: formalpara-title

   **Contents**

Specification of **all** communication partners (users, IT-systems, …)
with explanations of domain specific inputs and outputs or interfaces.
Optionally you can add domain specific formats or communication
protocols.

.. container:: formalpara-title

   **Motivation**

All stakeholders should understand which data are exchanged with the
environment of the system.

.. container:: formalpara-title

   **Form**

All kinds of diagrams that show the system as a black box and specify
the domain interfaces to communication partners.

Alternatively (or additionally) you can use a table. The title of the
table is the name of your system, the three columns contain the name of
the communication partner, the inputs, and the outputs.

**<Diagram or Table>**

**<optionally: Explanation of external domain interfaces>**

.. _`_technical_context`:

Technical Context
-----------------

.. container:: formalpara-title

   **Contents**

Technical interfaces (channels and transmission media) linking your
system to its environment. In addition a mapping of domain specific
input/output to the channels, i.e. an explanation which I/O uses which
channel.

.. container:: formalpara-title

   **Motivation**

Many stakeholders make architectural decision based on the technical
interfaces between the system and its context. Especially infrastructure
or hardware designers decide these technical interfaces.

.. container:: formalpara-title

   **Form**

E.g. UML deployment diagram describing channels to neighboring systems,
together with a mapping table showing the relationships between channels
and input/output.

**<Diagram or Table>**

**<optionally: Explanation of technical interfaces>**

**<Mapping Input/Output to Channels>**
