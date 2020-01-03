import falcon
import alphab

api = application = falcon.API()

api.add_route('/stockindex',alphab.stockindex())
api.add_route('/nyse',alphab.nyse())
api.add_route('/market_heat',alphab.market_heat())
api.add_route('/today_theme_z',alphab.today_theme_z())
api.add_route('/today_theme_d',alphab.today_theme_d())
api.add_route('/today_stock',alphab.today_stock())
api.add_route('/hot_pool',alphab.hot_pool())
api.add_route('/theme_pool',alphab.theme_pool())
api.add_route('/strong_pool',alphab.strong_pool())
api.add_route('/hit_pool',alphab.hit_pool())
api.add_route('/boom_pool',alphab.boom_pool())
api.add_route('/new_pool',alphab.new_pool())
api.add_route('/cnew_pool',alphab.cnew_pool())
api.add_route('/down_pool',alphab.down_pool())
api.add_route('/pre_hit_pool',alphab.pre_hit_pool())
api.add_route('/fast_pool',alphab.fast_pool())
api.add_route('/alphaa',alphab.alphaa())
api.add_route('/chart_sh',alphab.chart_sh())
api.add_route('/chart_sz',alphab.chart_sz())
api.add_route('/chart_cy',alphab.chart_cy())