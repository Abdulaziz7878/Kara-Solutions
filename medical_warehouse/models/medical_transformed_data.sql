{{config(materialized = "table")}}

with filtered_data As (
    SELECT *
    from {{source('public','channel_messages')}}
    
)

select 
    id,
    channel_title,
    channel_username,
    message,
    date
from filtered_data