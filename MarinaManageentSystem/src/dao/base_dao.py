class BaseDAO:
    def __init__(self, client, table):
        self.client = client
        self.table = table

    def insert(self, data):
        return self.client.table(self.table).insert(data).execute().data

    def select(self, filters=None):
        query = self.client.table(self.table).select("*")
        if filters:
            for key, value in filters.items():
                query = query.eq(key, value)
        return query.execute().data

    def update(self, record_id, data, id_field="id"):
        return (
            self.client.table(self.table)
            .update(data)
            .eq(id_field, record_id)
            .execute()
            .data
        )

    def delete(self, record_id, id_field="id"):
        return (
            self.client.table(self.table)
            .delete()
            .eq(id_field, record_id)
            .execute()
            .data
        )
