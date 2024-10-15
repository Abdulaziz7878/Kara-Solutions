{{ config(materialized='table') }}

select * 
from public.channel_messages