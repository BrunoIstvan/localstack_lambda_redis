import redis


def lambda_handler(event, context):

    # print(' >>>>> Antes de criar pool do redis')

    # pool = redis.ConnectionPool(host='172.17.0.2', port=6379, db=0)

    # print(' <<<<< Depois de criar pool do redis')

    # print('pool: ', pool)

    print(' >>>>> Antes de conectar ao redis usando o pool')

    r = redis.Redis(host='172.17.0.2', port=6379, db=0)

    print(' >>>>> Depois de conectar ao redis usando o pool')

    r.set('for', 'bar')

    value = r.get('for')
    # value = 'test'

    obj = {'message': f'{value}'}
    print(obj)
    return obj


if __name__ == '__main__':
    lambda_handler(None, None)