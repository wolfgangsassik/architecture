.. _section-introduction-and-goals:

Introduction and Goals
======================

Describes the relevant requirements and the driving forces that software
architects and development team must consider. These include

-  underlying business goals,

-  essential features,

-  essential functional requirements,

-  quality goals for the architecture and

-  relevant stakeholders and their expectations

.. _`_requirements_overview`:

Requirements Overview
---------------------

.. container:: formalpara-title

   **Contents**

Short description of the functional requirements, driving forces,
extract (or abstract) of requirements. Link to (hopefully existing)
requirements documents (with version number and information where to
find it).

.. container:: formalpara-title

   **Motivation**

From the point of view of the end users a system is created or modified
to improve support of a business activity and/or improve the quality.

.. container:: formalpara-title

   **Form**

Short textual description, probably in tabular use-case format. If
requirements documents exist this overview should refer to these
documents.

Keep these excerpts as short as possible. Balance readability of this
document with potential redundancy w.r.t to requirements documents.

See `Introduction and Goals <https://docs.arc42.org/section-1/>`__ in
the arc42 documentation.

.. _`_quality_goals`:

Quality Goals
-------------

.. container:: formalpara-title

   **Contents**

The top three (max five) quality goals for the architecture whose
fulfillment is of highest importance to the major stakeholders. We
really mean quality goals for the architecture. Don’t confuse them with
project goals. They are not necessarily identical.

Consider this overview of potential topics (based upon the ISO 25010
standard):

.. image:: images/2_iso-25010-topics-EN.drawio.png
   :alt: Categories of Quality Requirements

.. container:: formalpara-title

   **Motivation**

You should know the quality goals of your most important stakeholders,
since they will influence fundamental architectural decisions. Make sure
to be very concrete about these qualities, avoid buzzwords. If you as an
architect do not know how the quality of your work will be judged…

.. container:: formalpara-title

   **Form**

A table with quality goals and concrete scenarios, ordered by priorities

.. _`_stakeholders`:

Stakeholders
------------

.. container:: formalpara-title

   **Contents**

Explicit overview of stakeholders of the system, i.e. all person, roles
or organizations that

-  should know the architecture

-  have to be convinced of the architecture

-  have to work with the architecture or with code

-  need the documentation of the architecture for their work

-  have to come up with decisions about the system or its development

.. container:: formalpara-title

   **Motivation**

You should know all parties involved in development of the system or
affected by the system. Otherwise, you may get nasty surprises later in
the development process. These stakeholders determine the extent and the
level of detail of your work and its results.

.. container:: formalpara-title

   **Form**

Table with role names, person names, and their expectations with respect
to the architecture and its documentation.

+-------------+---------------------------+---------------------------+
| Role/Name   | Contact                   | Expectations              |
+=============+===========================+===========================+
| *<Role-1>*  | *<Contact-1>*             | *<Expectation-1>*         |
+-------------+---------------------------+---------------------------+
| *<Role-2>*  | *<Contact-2>*             | *<Expectation-2>*         |
+-------------+---------------------------+---------------------------+
