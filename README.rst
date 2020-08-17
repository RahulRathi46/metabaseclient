Metabase Client
========================

A python wrapper for metabase api

--------------

Index

- Installation
- Basic Usage

---------------

Installation

``pip install MetabaseClient``


------------------

Basic Usage

- import py package

    import MetabaseClient as MC

- init client

    client = MC.Client(url,username,password)

- Stored Queries or Cards

    client.card().get()

- Stored dashboard

    client.dashboard().get()

- Get Utils

    client.utils()

---------------------

Full Documentation : https://github.com/vangiex/metabaseclient/wiki




