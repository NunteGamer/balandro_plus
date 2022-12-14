# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] >= 3: PY3 = True
else: PY3 = False


from platformcode import config, logger
from core.item import Item

from core import channeltools


color_list_prefe = config.get_setting('channels_list_prefe_color', default='gold')
color_list_proxies = config.get_setting('channels_list_proxies_color', default='red')
color_list_inactive = config.get_setting('channels_list_inactive_color', default='gray')

color_alert = config.get_setting('notification_alert_color', default='red')
color_infor = config.get_setting('notification_infor_color', default='pink')
color_adver = config.get_setting('notification_adver_color', default='violet')
color_avis = config.get_setting('notification_avis_color', default='yellow')
color_exec = config.get_setting('notification_exec_color', default='cyan')


context_buscar = []

tit = '[COLOR %s][B]Información ajustes buscar[/B][/COLOR]' % color_infor
context_buscar.append({'title': tit, 'channel': 'search', 'action': 'show_help_parameters'})

tit = '[COLOR %s]Información menús[/COLOR]' % color_avis
context_buscar.append({'title': tit, 'channel': 'helper', 'action': 'show_menu_parameters'})

tit = '[COLOR %s][B]Global configurar proxies[/B][/COLOR]' % color_list_proxies
context_buscar.append({'title': tit, 'channel': 'proxysearch', 'action': 'proxysearch_all'})

if config.get_setting('proxysearch_excludes', default=''):
    tit = '[COLOR %s]Anular canales excluidos de Proxies[/COLOR]' % color_adver
    context_buscar.append({'title': tit, 'channel': 'proxysearch', 'action': 'channels_proxysearch_del'})

tit = '[COLOR %s]Información proxies[/COLOR]' % color_infor
context_buscar.append({'title': tit, 'channel': 'helper', 'action': 'show_help_proxies'})

tit = '[COLOR %s][B]Quitar proxies actuales[/B][/COLOR]' % color_list_proxies
context_buscar.append({'title': tit, 'channel': 'actions', 'action': 'manto_proxies'})

tit = '[COLOR %s]Información búsquedas[/COLOR]' % color_infor
context_buscar.append({'title': tit, 'channel': 'search', 'action': 'show_help'})

tit = '[COLOR %s]Ajustes categorías buscar y proxies[/COLOR]' % color_exec
context_buscar.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})


context_proxy_channels = []

tit = '[COLOR %s]Información menús[/COLOR]' % color_infor
context_proxy_channels.append({'title': tit, 'channel': 'helper', 'action': 'show_menu_parameters'})

tit = '[COLOR %s]Información proxies[/COLOR]' % color_avis
context_proxy_channels.append({'title': tit, 'channel': 'helper', 'action': 'show_help_proxies'})

tit = '[COLOR %s]Ajustes categorías menú y proxies[/COLOR]' % color_exec
context_proxy_channels.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})


context_cfg_search = []

tit = '[COLOR %s]Información menús[/COLOR]' % color_infor
context_cfg_search.append({'title': tit, 'channel': 'helper', 'action': 'show_menu_parameters'})

tit = '[COLOR %s]Ajustes categoría menú[/COLOR]' % color_exec
context_cfg_search.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})


context_torrents = []

if config.get_setting('cliente_torrent') == 'Seleccionar' or config.get_setting('cliente_torrent') == 'Ninguno':
    tit = '[COLOR %s][B]Información Motores torrents[/B][/COLOR]' % color_infor
    context_torrents.append({'title': tit, 'channel': 'helper', 'action': 'show_help_torrents'})

tit = '[COLOR %s][B]Motores torrents instalados[/B][/COLOR]' % color_avis
context_torrents.append({'title': tit, 'channel': 'helper', 'action': 'show_clients_torrent'})

tit = '[COLOR %s]Información menús[/COLOR]' % color_infor
context_torrents.append({'title': tit, 'channel': 'helper', 'action': 'show_channels_parameters'})

tit = '[COLOR %s]Ajustes categorías canales, torrents y buscar[/COLOR]' % color_exec
context_torrents.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})


context_parental = []

if config.get_setting('adults_password'):
    tit = '[COLOR %s][B]Eliminar Pin parental[/B][/COLOR]' % color_adver
    context_parental.append({'title': tit, 'channel': 'actions', 'action': 'adults_password_del'})
else:
    tit = '[COLOR %s][B]Información parental[/B][/COLOR]' % color_infor
    context_parental.append({'title': tit, 'channel': 'helper', 'action': 'show_help_adults'})

tit = '[COLOR %s]Información menús[/COLOR]' % color_avis
context_parental.append({'title': tit, 'channel': 'helper', 'action': 'show_channels_parameters'})

tit = '[COLOR %s]Ajustes categorías canales y parental[/COLOR]' % color_exec
context_parental.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})


def mainlist(item):
    logger.info()
    itemlist = []

    item.category = 'Agrupaciones de Canales'

    if config.get_setting('mnu_search_proxy_channels', default=False):
        itemlist.append(item.clone( channel='submnuctext', action='submnu_search', title='[B]Buscar Nuevos Proxies[/B]', context=context_proxy_channels,
                                    only_options_proxies = True, thumbnail=config.get_thumb('flame'), text_color='red' ))

    if config.get_setting('sub_mnu_cfg_search', default=True):
        itemlist.append(item.clone( channel='submnuctext', action='submnu_search', title= '[B]Personalizar búsquedas[/B]', context=context_cfg_search,
                                    thumbnail=config.get_thumb('settings'), text_color='moccasin', extra = 'all' ))

    if not item.mnu_lang:
        itemlist.append(Item( channel='search', action='mainlist', title='[B]Buscar[/B]', context=context_buscar,
                              thumbnail=config.get_thumb('search'), text_color='yellow' ))

        itemlist.append(item.clone( action='', title= '[B]Agrupaciones:[/B]', text_color='lightyellow', folder=False ))

        if config.get_setting('channels_link_pyse', default=False) or config.get_setting('mnu_pelis', default=True) or config.get_setting('mnu_series', default=True):
            itemlist.append(item.clone( title = ' - [B]Novedades[/B]', thumbnail=config.get_thumb('heart'), action = 'submnu_news', text_color='yellowgreen' ))

        itemlist.append(item.clone( title = ' - [B]Películas y/ó Series[/B]', action = 'submnu_alls',
                                    thumbnail=config.get_thumb('booklet'), text_color='goldenrod' ))

        if config.get_setting('channels_link_pyse', default=False) or config.get_setting('mnu_pelis', default=True):
            itemlist.append(item.clone( title = ' - [B]Películas[/B]', action = 'submnu_pelis', thumbnail=config.get_thumb('movie'), text_color='deepskyblue' ))

        if config.get_setting('channels_link_pyse', default=False) or config.get_setting('mnu_series', default=True):
            itemlist.append(item.clone( title = ' - [B]Series[/B]', action = 'submnu_series', thumbnail=config.get_thumb('tvshow'), text_color='hotpink' ))

        if config.get_setting('mnu_documentales', default=True):
            itemlist.append(item.clone( title = ' - [B]Documentales[/B]', action = 'submnu_docs', thumbnail=config.get_thumb('documentary'), text_color='cyan' ))

        presentar = True
        if config.get_setting('mnu_simple', default=False): presentar = False

        if presentar:
            if config.get_setting('mnu_doramas', default=True):
                itemlist.append(item.clone( title = ' - [B]Doramas[/B]', action = 'submnu_doramas', thumbnail=config.get_thumb('computer'), text_color='firebrick' ))

        presentar = True
        descartar_xxx = config.get_setting('descartar_xxx', default=False)

        if config.get_setting('mnu_simple', default=False): presentar = False
        else:
           if descartar_xxx:
               if descartar_anime: presentar = False

        if presentar:
            if not config.get_setting('descartar_anime', default=True):
                itemlist.append(item.clone( title = ' - [B]Animes[/B]', action = 'submnu_animes', thumbnail=config.get_thumb('anime'), text_color='springgreen' ))

            if not descartar_xxx:
                itemlist.append(item.clone( title = ' - [B]Adultos (+18)[/B]', action = 'submnu_adults', thumbnail=config.get_thumb('adults'), text_color='orange' ))

        itemlist.append(item.clone( title = ' - [B]Diversos[/B]', action = 'submnu_diversos', thumbnail=config.get_thumb('crossroads'), text_color='fuchsia' ))

    presentar = False
    if item.mnu_lang: presentar = True
    else:
       if config.get_setting('mnu_idiomas', default=True): presentar = False

    if presentar:
        itemlist.append(item.clone( title = '[B]Audios:[/B]', action = '', thumbnail=config.get_thumb('idiomas'), text_color='violet' ))
        itemlist.append(item.clone( title = ' - Canales con Audio Múltiple', action = 'ch_groups', group = 'all', extra = 'mixed' ))
        itemlist.append(item.clone( title = ' - Canales con Audio solo en Castellano', action = 'ch_groups', group = 'cast', extra = 'mixed' ))
        itemlist.append(item.clone( title = ' - Canales con Audio solo en Latino', action = 'ch_groups', group = 'lat', extra = 'mixed' ))
        itemlist.append(item.clone( title = ' - Canales con Audio solo en Vose', action = 'ch_groups', group = 'vose', extra = 'mixed' ))
        itemlist.append(item.clone( title = ' - Canales con Audio solo en VO', action = 'ch_groups', group = 'vo', extra = 'mixed' ))
    else:
        itemlist.append(item.clone( title = ' - [B]Audios[/B]', action = 'submnu_audios', thumbnail=config.get_thumb('idiomas'), text_color='violet' ))

    return itemlist


def submnu_news(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Novedades:[/B]', thumbnail=config.get_thumb('heart'), action = '', text_color='yellowgreen' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( channel='tmdblists', action='listado', title= ' - Películas en Cartelera [COLOR violet](Listas TMDB)[/COLOR]',
                                    extra='now_playing', thumbnail=config.get_thumb('movie'), search_type = 'movie' ))

    if config.get_setting('mnu_pelis', default=True):
        itemlist.append(item.clone( title = ' - Canales de [COLOR deepskyblue]Películas[/COLOR] con Estrenos y/ó Novedades',
                                    thumbnail=config.get_thumb('movie'), action = 'ch_groups', group = 'news', extra = 'movies', ))

    if config.get_setting('mnu_series', default=True):
        itemlist.append(item.clone( title = ' - Canales de [COLOR hotpink]Series[/COLOR] con Episodios Nuevos y/ó Últimos',
                                    thumbnail=config.get_thumb('tvshow'), action = 'ch_groups', group = 'lasts', extra = 'tvshows' ))

    return itemlist


def submnu_alls(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Películas y/ó Series[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='goldenrod' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( title = '[B]Listas:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='violet' ))

        itemlist.append(item.clone( channel='tmdblists', action='listado', title= '   - Películas Más populares [COLOR violet]TMDB[/COLOR]', extra='popular',
                                    thumbnail=config.get_thumb('bestmovies'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='tmdblists', action='listado', title= '   - Películas Más valoradas [COLOR violet]TMDB[/COLOR]',
                                    extra='top_rated', thumbnail=config.get_thumb('bestmovies'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_bestmovies', title='   - Películas Recomendadas [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('bestmovies'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='tmdblists', action='listado', title= '   - Series Más populares [COLOR violet]TMDB[/COLOR]',
                                    extra='popular', thumbnail=config.get_thumb('besttvshows'), search_type = 'tvshow' ))

        itemlist.append(item.clone( channel='tmdblists', action='listado', title= '   - Series Más valoradas [COLOR violet]TMDB[/COLOR]',
                                    extra='top_rated', thumbnail=config.get_thumb('besttvshows'), search_type = 'tvshow' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_besttvshows', title='   - Series Recomendadas [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('besttvshows'), search_type = 'tvshow' ))

    itemlist.append(item.clone( title = '[B]Canales:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='gold' ))

    itemlist.append(item.clone( title = '   - Con temática Clásica', action = 'ch_groups', group = 'classic', extra = 'all' ))

    if config.get_setting('mnu_infantiles', default=True):
        itemlist.append(item.clone( title = '   - Con temática Infantil', action = 'ch_groups', group = 'kids', extra = 'all' ))

    if config.get_setting('mnu_torrents', default=True):
        itemlist.append(item.clone( title = '   - Que pueden tener enlaces Torrents', context=context_torrents,
                                    thumbnail=config.get_thumb('torrents'), action = 'ch_groups', group = 'torrents', extra = 'torrents' ))

    itemlist.append(item.clone( title = '   - Con Rankings (Más vistas, Más valoradas, etc.)', action = 'ch_groups', group = 'rankings', extra = 'all' ))

    if config.get_setting('mnu_idiomas', default=True):
        itemlist.append(item.clone( title = '   - Con Vídeos en Versión Original y/ó Subtitulada', action = 'ch_groups', group = 'vos', extra = 'all' ))

    itemlist.append(item.clone( title = '   - Con Vídeos en 3D', action = 'ch_groups', group = '3d', extra = 'all' ))

    return itemlist


def submnu_pelis(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Películas[/B]', action = '', thumbnail=config.get_thumb('movie'), text_color='deepskyblue' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( title = '[B]Listas:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='violet' ))

        itemlist.append(item.clone( channel='tmdblists', action='generos', title='   - Por género [COLOR violet]TMDB[/COLOR]',
                                    thumbnail=config.get_thumb('listgenres'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='tmdblists', action='anios', title='   - Por año [COLOR violet]TMDB[/COLOR]',
                                    thumbnail=config.get_thumb('listyears'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_years', title='   - Por año [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('listyears'), search_type = 'movie' ))

    itemlist.append(item.clone( title = '[B]Canales:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='gold' ))

    if config.get_setting('mnu_generos', default=True):
        itemlist.append(item.clone( title = '   - Con Géneros', action = 'ch_groups', group = 'genres', extra = 'movies' ))

    itemlist.append(item.clone( title = '   - Con Idiomas', action = 'ch_groups', group = 'languages', extra = 'movies' ))
    itemlist.append(item.clone( title = '   - Con Años', action = 'ch_groups', group = 'years', extra = 'movies' ))
    itemlist.append(item.clone( title = '   - Con Épocas', action = 'ch_groups', group = 'epochs', extra = 'movies' ))
    itemlist.append(item.clone( title = '   - Con Calidades', action = 'ch_groups', group = 'qualityes', extra = 'movies' ))

    presentar = False
    if config.get_setting('channels_link_pyse', default=False): presentar = True
    elif config.get_setting('mnu_pelis', default=True): presentar = True

    if presentar:
        itemlist.append(item.clone( title = '   - Con Países', action = 'ch_groups', group = 'countries', extra = 'movies' ))

    return itemlist


def submnu_series(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Series[/B]', action = '', thumbnail=config.get_thumb('tvshow'), text_color='hotpink' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( title = '[B]Listas:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='violet' ))

        itemlist.append(item.clone( channel='tmdblists', action='listado', title= '   - En emisión [COLOR violet]TMDB[/COLOR]',
                                             extra='on_the_air', thumbnail=config.get_thumb('tvshow'), search_type = 'tvshow' ))

        itemlist.append(item.clone( channel='tmdblists', action='generos', title='   - Por género [COLOR violet]TMDB[/COLOR]',
                                    thumbnail=config.get_thumb('listgenres'), search_type = 'tvshow' ))

        itemlist.append(item.clone( channel='tmdblists', action='anios', title='   - Por año [COLOR violet]TMDB[/COLOR]',
                                   thumbnail=config.get_thumb('listyears'), search_type = 'tvshow' ))

    itemlist.append(item.clone( title = '[B]Canales:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='gold' ))

    if config.get_setting('mnu_generos', default=True):
        itemlist.append(item.clone( title = ' -   Con Géneros', action = 'ch_groups', group = 'genres', extra = 'tvshows' ))

    if config.get_setting('mnu_novelas', default=True):
        itemlist.append(item.clone( title = ' -   Con Novelas', action = 'ch_groups', group = 'tales', extra = 'tvshows' ))

    presentar = False
    if config.get_setting('channels_link_pyse', default=False): presentar = True
    elif not config.get_setting('mnu_series', default=True): presentar = True

    if presentar:
        itemlist.append(item.clone( title = ' -   Con Países', action = 'ch_groups', group = 'countries', extra = 'tvshows' ))

    return itemlist


def submnu_docs(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Documentales:[/B]', action = '', thumbnail=config.get_thumb('documentary'), text_color='cyan' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( channel='filmaffinitylists', action='_bestdocumentaries', title=' - Los Mejores [COLOR violet](Listas Filmaffinity)[/COLOR]',
                                    thumbnail=config.get_thumb('bestdocumentaries'), search_type = 'all' ))

    itemlist.append(item.clone( title = ' - Canales con temática [COLOR cyan]Documental[/COLOR]', action = 'ch_groups', group = 'docs' ))

    return itemlist


def submnu_doramas(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Doramas:[/B]', action = '', thumbnail=config.get_thumb('computer'), text_color='firebrick' ))

    itemlist.append(item.clone( title = ' - [COLOR magenta][B]Todos los canales con contenido de Doramas[/B][/COLOR]',
                                action = 'ch_groups', group = 'dorama' ))

    itemlist.append(item.clone( title = ' - Solo los canales con contenido Exclusivo de [COLOR firebrick]Doramas[/COLOR]',
                                action = 'ch_groups', group = 'dorama', only = 'doramas', search_special = 'dorama' ))

    return itemlist


def submnu_animes(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Animes:[/B]', action = '', thumbnail=config.get_thumb('anime'), text_color='springgreen' ))

    itemlist.append(item.clone( title = ' - [COLOR magenta][B]Todos los canales con contenido de Animes[/B][/COLOR]',
                                action = 'ch_groups', group = 'anime', context=context_parental ))

    itemlist.append(item.clone( title = ' - Solo los canales con contenido Exclusivo de [COLOR springgreen]Animes[/COLOR]',
                                action = 'ch_groups', group = 'anime', only = 'animes', search_special = 'anime' ))

    return itemlist


def submnu_adults(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Adultos (+18):[/B]', action = '', thumbnail=config.get_thumb('adults'), text_color='orange' ))

    itemlist.append(item.clone( title = ' - [COLOR magenta][B]Todos los canales que pueden contener vídeos para Adultos[/B][/COLOR]',
                                action = 'ch_groups', group = 'adults', context=context_parental ))

    itemlist.append(item.clone( title = ' - Solo los canales con contenido Exclusivo de [COLOR orange]Adultos[/COLOR]',
                                action = 'ch_groups', group = 'adults', only = 'adults' ))

    return itemlist


def submnu_diversos(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = '[B]Diversos[/B]', action = '', thumbnail=config.get_thumb('crossroads'), text_color='fuchsia' ))

    if config.get_setting('search_extra_main', default=False):
        itemlist.append(item.clone( title = '[B]Personas:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='violet' ))

        itemlist.append(item.clone( channel='tmdblists', action='personas', search_type='cast', title='   - Buscar intérprete ... [COLOR violet]TMDB[/COLOR]',
                                    plot = 'Escribir el nombre de un actor o una actriz para listar todas las películas y series en las que ha intervenido.' ))

        itemlist.append(item.clone( channel='tmdblists', action='personas', search_type='crew', title='   - Buscar dirección ... [COLOR violet]TMDB[/COLOR]',
                                    plot = 'Escribir el nombre de una persona para listar todas las películas y series que ha dirigido.' ))

        itemlist.append(item.clone( title = '[B]Listas:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='violet' ))

        itemlist.append(item.clone( channel='tmdblists', action='networks', title='   - Por productora [COLOR violet]TMDB[/COLOR]',
                                    thumbnail=config.get_thumb('movie'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='plataformas', title='   - Por plataforma [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('heart'), search_type = 'all' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_themes', title='   - Por tema [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('listthemes'), search_type = 'all' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_oscars', title='   - Premios Oscar [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('oscars'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_sagas', title='   - Sagas y colecciones [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('bestsagas'), search_type = 'movie' ))

        itemlist.append(item.clone( channel='filmaffinitylists', action='_emmys', title='   - Premios Emmy [COLOR violet]Filmaffinity[/COLOR]',
                                    thumbnail=config.get_thumb('emmys'), origen='mnu_esp', search_type = 'tvshow' ))

    itemlist.append(item.clone( title = '[B]Canales:[/B]', action = '', thumbnail=config.get_thumb('booklet'), text_color='gold' ))

    itemlist.append(item.clone( title = '   - Con Categorías', action = 'ch_groups', group = 'categories', extra = 'mixed' ))
    itemlist.append(item.clone( title = '   - Con Intérpretes', action = 'ch_groups', group = 'stars', extra = 'mixed' ))
    itemlist.append(item.clone( title = '   - Con Directores/as', action = 'ch_groups', group = 'directors', extra = 'mixed' ))
    itemlist.append(item.clone( title = '   - Con Productoras, Plataformas, y/ó Estudios', action = 'ch_groups', group = 'producers', extra = 'mixed' ))
    itemlist.append(item.clone( title = '   - Con Listas, Sagas, Colecciones, y/ó Otros', action = 'ch_groups', group = 'lists', extra = 'mixed' ))

    return itemlist


def submnu_audios(item):
    logger.info()
    itemlist = []


    itemlist.append(item.clone( title = '[B]Audios:[/B]', action = '', thumbnail=config.get_thumb('idiomas'), text_color='violet' ))
    itemlist.append(item.clone( title = ' - Canales con Audio Múltiple', action = 'ch_groups', group = 'all', extra = 'mixed' ))
    itemlist.append(item.clone( title = ' - Canales con Audio solo en Castellano', action = 'ch_groups', group = 'cast', extra = 'mixed' ))
    itemlist.append(item.clone( title = ' - Canales con Audio solo en Latino', action = 'ch_groups', group = 'lat', extra = 'mixed' ))
    itemlist.append(item.clone( title = ' - Canales con Audio solo en Vose', action = 'ch_groups', group = 'vose', extra = 'mixed' ))
    itemlist.append(item.clone( title = ' - Canales con Audio solo en VO', action = 'ch_groups', group = 'vo', extra = 'mixed' ))

    return itemlist


def ch_groups(item):
    logger.info()
    itemlist = []

    descartar_xxx = config.get_setting('descartar_xxx', default=False)
    descartar_anime = config.get_setting('descartar_anime', default=False)

    accion = 'mainlist'

    search_type = ''
    if item.group == 'news': accion = 'mainlist_pelis'
    elif item.group == 'lasts': accion = 'mainlist_series'

    elif item.group == 'genres' or item.group == 'generos':
         if item.extra == 'movies': search_type = 'movie'
         else: search_type = 'tvshow'

    elif item.group == 'languages':
         accion = 'idiomas'
         search_type = 'movie'
    elif item.group == 'years':
         accion = 'anios'
         search_type = 'movie'
    elif item.group == 'epochs':
         search_type = 'movie'

    elif item.group == 'countries':
         if item.extra == 'movies':
             accion = 'paises'
             search_type = 'movie'
         else:
             accion = 'mainlist_series'
             search_type = 'tvshow'

    elif item.group == 'qualityes':
         accion = 'calidades'
         search_type = 'movie'

    elif item.group == 'categories': accion = 'categorias'

    canales = []
    filtros = {}

    channels_list_status = config.get_setting('channels_list_status', default=0)
    if channels_list_status > 0:
        filtros['status'] = 0 if channels_list_status == 1 else 1

    ch_list = channeltools.get_channels_list(filtros=filtros)

    i = 0

    for ch in ch_list:
        if ch['status'] == -1: continue

        try: agrupaciones = ch['clusters']
        except: continue

        if config.get_setting('mnu_problematicos', default=False):
            if 'problematic' in ch['clusters']: continue

        if 'trailers' in ch['clusters']: continue

        if item.group == 'genres' or item.group == 'generos':
            if item.extra == 'movies':
                if not 'movie' in ch['categories']: continue
                if not 'géneros' in ch['notes']: continue

            if item.extra == 'tvshows':
                if not 'tvshow' in ch['categories']: continue
                if not 'Géneros' in ch['notes']: continue

            search_types = ch['search_types']

            accion = 'generos'

            if item.group == 'generos': accion = 'mainlist'
            elif 'all' in search_types:
               if search_type == 'tvshow':
                   if not 'Géneros' in ch['notes']: continue
               elif not 'géneros' in ch['notes']: accion = 'mainlist'

        elif item.group == 'countries':
            if not 'countries' in ch['clusters']: continue

            search_types = ch['search_types']

            if item.extra == 'movies':
                if not 'movie' in search_types: continue
            else:
                if not 'tvshow' in search_types: continue

        elif item.group == 'cast':
            audios = ch['language']
            if not item.group in audios: continue

            if 'lat' in audios: continue
            elif 'vose' in audios: continue
            elif 'vo' in audios: continue
        elif item.group == 'lat':
            audios = ch['language']
            if not item.group in audios: continue

            if 'cast' in audios: continue
            elif 'vose' in audios: continue
            elif 'vo' in audios: continue
        elif item.group == 'vose':
            audios = ch['language']
            if not item.group in audios: continue

            if 'cast' in audios: continue
            elif 'lat' in audios: continue
            elif 'vo' in audios: continue
        elif item.group == 'vo':
            audios = ch['language']
            if not item.group in audios: continue

            if 'cast' in audios: continue
            elif 'lat' in audios: continue
            elif 'vose' in audios: continue

            if ch['searchable'] == False: # adultos
               if descartar_xxx: continue

        elif item.group == 'all':
            audios = ch['language']
            if len(audios) == 1: continue

        else:
           if not item.group in agrupaciones: continue

        if ch['searchable'] == False: # adultos
            if descartar_xxx:
                if 'adults' in agrupaciones:
                    if item.group == 'news': continue
                    elif item.group == 'rankings': continue
                    elif item.group == 'categories': continue
                    elif item.group == 'stars': continue
                    elif item.group == 'vose': continue
                    elif item.group == 'vo': continue
            elif descartar_anime:
                if 'anime' in agrupaciones:
                   if item.group == 'anime': continue
                   elif item.group == 'vose': continue
                   elif item.group == 'vo': continue

            if not config.get_setting('mnu_doramas', default=True):
                if 'dorama' in ch['clusters']: continue

            if not config.get_setting('mnu_animes', default=True):
                if 'anime' in agrupaciones: continue

            if not config.get_setting('mnu_adultos', default=True):
                if 'adults' in agrupaciones: continue

        action = accion

        if item.group == 'dorama':
            if item.only == 'doramas':
                if not str(ch['clusters']) == "['dorama']":
                    if not str(ch['clusters']) == "['current', 'dorama']":
                        continue

        elif item.group == 'anime':
            if item.only == 'animes':
                if not str(ch['clusters']) == "['anime']":
                    if not str(ch['clusters']) == "['current', 'anime']":
                        continue

            if 'anime' in ch['notes'].lower(): action = 'mainlist_anime'
            else:
                 if ch['name'].startswith('Series'): action = 'mainlist_series'
                 else:
                     if ch['name'] == 'Tekilaz': action = 'mainlist_series'
                     else: action = 'mainlist_pelis'

        elif item.group == 'adults':
            if item.only == 'adults':
                if not str(ch['clusters']) == "['adults']":
                    if not str(ch['clusters']) == "['current', 'adults']":
                        continue

        context = []

        cfg_proxies_channel = 'channel_' + ch['id'] + '_proxies'

        if 'proxies' in ch['notes'].lower():
            if config.get_setting(cfg_proxies_channel, default=''):
                tit = '[COLOR %s][B]Quitar los proxies del canal[/B][/COLOR]' % color_list_proxies
                context.append({'title': tit, 'channel': item.channel, 'action': '_quitar_proxies'})

        if ch['status'] != 1:
            tit = '[COLOR %s][B]Marcar canal como Preferido[/B][/COLOR]' % color_list_prefe
            context.append({'title': tit, 'channel': item.channel, 'action': '_marcar_canal', 'estado': 1})

        if ch['status'] != 0:
            if ch['status'] == 1:
                tit = '[COLOR %s][B]Des-Marcar canal como Preferido[/B][/COLOR]' % color_list_prefe
                context.append({'title': tit, 'channel': item.channel, 'action': '_marcar_canal', 'estado': 0})
            elif ch['status'] == -1:
                tit = '[COLOR %s][B]Des-Marcar canal como Desactivado[/B][/COLOR]' % color_list_inactive
                context.append({'title': tit, 'channel': item.channel, 'action': '_marcar_canal', 'estado': 0})
            else:
                tit = '[COLOR white][B]Marcar canal como Activo[/B][/COLOR]'
                context.append({'title': tit, 'channel': item.channel, 'action': '_marcar_canal', 'estado': 0})

        if ch['status'] != -1:
            tit = '[COLOR %s][B]Marcar canal como Desactivado[/B][/COLOR]' % color_list_inactive
            context.append({'title': tit, 'channel': item.channel, 'action': '_marcar_canal', 'estado': -1})

        cfg_domains = False

        if 'current' in ch['clusters']:
            cfg_domains = True

            tit = '[COLOR %s]Información Dominios[/COLOR]' % color_infor
            context.append({'title': tit, 'channel': 'helper', 'action': 'show_help_domains'})

            tit = '[COLOR yellowgreen][B]Dominio vigente[/B][/COLOR]'
            context.append({'title': tit, 'channel': item.channel, 'action': '_dominio_vigente'})

            tit = '[COLOR darkorange][B]Modificar dominio Memorizado[/B][/COLOR]'
            context.append({'title': tit, 'channel': item.channel, 'action': '_dominio_memorizado'})

            tit = '[COLOR %s][B]Configurar dominio a usar[/B][/COLOR]' % color_adver
            context.append({'title': tit, 'channel': item.channel, 'action': '_dominios'})

        if 'register' in ch['clusters']:
            cfg_user_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_username'
            cfg_pass_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_password'

            if not config.get_setting(cfg_user_channel, default='') or not config.get_setting(cfg_pass_channel, default=''):
                tit = '[COLOR green][B]Información para Registrarse[/B][/COLOR]'
                context.append({'title': tit, 'channel': 'helper', 'action': 'show_help_register'})

                tit = '[COLOR teal][B]Credenciales Cuenta[/B][/COLOR]'
                context.append({'title': tit, 'channel': item.channel, 'action': '_credenciales'})
            else:
               cfg_login_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_login'

               presentar = True
               if 'dominios' in ch['notes'].lower():
                   cfg_dominio_channel = 'channel_' + ch['id'] + '_dominio'
                   if not config.get_setting(cfg_dominio_channel, default=''): presentar = False

               if presentar:
                   if config.get_setting(cfg_login_channel, default=False):
                       tit = '[COLOR teal][B]Cerrar sesión[/B][/COLOR]'
                       context.append({'title': tit, 'channel': item.channel, 'action': '_credenciales'})

        if 'proxies' in ch['notes'].lower():
            if not config.get_setting(cfg_proxies_channel, default=''):
                tit = '[COLOR %s]Información proxies[/COLOR]' % color_infor
                context.append({'title': tit, 'channel': 'helper', 'action': 'show_help_proxies'})

            tit = '[COLOR %s][B]Configurar proxies a usar[/B][/COLOR]' % color_list_proxies
            context.append({'title': tit, 'channel': item.channel, 'action': '_proxies'})

        tit = '[COLOR darkorange][B]Test Web del canal[/B][/COLOR]'
        context.append({'title': tit, 'channel': item.channel, 'action': '_tests'})

        if cfg_domains:
            tit = '[COLOR %s]Ajustes categoría dominios[/COLOR]' % color_exec
            context.append({'title': tit, 'channel': 'actions', 'action': 'open_settings'})

        color = color_list_prefe if ch['status'] == 1 else 'white' if ch['status'] == 0 else color_list_inactive

        plot = ''
        plot += '[' + ', '.join([config.get_localized_category(ct) for ct in ch['categories']]) + '][CR]'
        plot += '[' + ', '.join([idioma_canal(lg) for lg in ch['language']]) + ']'
        if ch['notes'] != '': plot += '[CR][CR]' + ch['notes']

        titulo = ch['name']

        if ch['status'] == -1:
            titulo += '[I][COLOR %s] (desactivado)[/COLOR][/I]' % color_list_inactive
            if config.get_setting(cfg_proxies_channel, default=''): titulo += '[I][COLOR %s] (proxies)[/COLOR][/I]' % color_list_proxies
        else:
            if config.get_setting(cfg_proxies_channel, default=''):
                if ch['status'] == 1: titulo += '[I][COLOR %s] (proxies)[/COLOR][/I]' % color_list_proxies
                else: color = color_list_proxies

        if 'register' in ch['clusters']:
            cfg_user_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_username'
            cfg_pass_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_password'
            if not config.get_setting(cfg_user_channel, default='') or not config.get_setting(cfg_pass_channel, default=''):
               titulo += '[I][COLOR teal] (cuenta)[/COLOR][/I]'
            else:
               cfg_login_channel = 'channel_' + ch['id'] + '_' + ch['id'] +'_login'

               if config.get_setting(cfg_login_channel, default=False):
                   presentar = True
                   if 'dominios' in ch['notes'].lower():
                       cfg_dominio_channel = 'channel_' + ch['id'] + '_dominio'
                       if not config.get_setting(cfg_dominio_channel, default=''): presentar = False

                   if presentar: titulo += '[I][COLOR teal] (sesion)[/COLOR][/I]'

        if not PY3:
            if 'mismatched' in ch['clusters']: titulo += '[I][COLOR coral] (Incompatible)[/COLOR][/I]'

        if 'inestable' in ch['clusters']: titulo += '[I][COLOR plum] (inestable)[/COLOR][/I]'

        if 'problematic' in ch['clusters']: titulo += '[I][COLOR darkgoldenrod] (problemático)[/COLOR][/I]'

        i =+ 1

        itemlist.append(Item( channel=ch['id'], action=accion, title=titulo, context=context,
                                                text_color=color, plot = plot, thumbnail=ch['thumbnail'], category=ch['name'],
                                                search_type = search_type, sort = 'C' ))

        canales.append(ch['id'])

    if len(itemlist) == 0 or i == 0:
        itemlist.append(item.clone( channel='filters', action='channels_status', title='[B]Opción Sin canales Preferidos[/B]', text_color=color_list_prefe,
                                    des_rea=False, thumbnail=config.get_thumb('stack'), sort = 'C', folder=False ))

    if itemlist:
        buscar_only_group = True

        if item.group == 'adults': buscar_only_group = False

        if buscar_only_group:
            if len(itemlist) > 1:
                if config.get_setting('mnu_search_proxy_channels', default=False):
                    itemlist.append(item.clone( channel='submnuctext', action='submnu_search', title='[B]Buscar Nuevos Proxies[/B]', context=context_proxy_channels,
                                                only_options_proxies = True, thumbnail=config.get_thumb('flame'), text_color='red' ))

                if config.get_setting('sub_mnu_cfg_search', default=True):
                    itemlist.append(item.clone( channel='submnuctext', action='submnu_search', title= '[B]Personalizar búsquedas[/B]', context=context_cfg_search,
                                                extra = item.extra, thumbnail=config.get_thumb('settings'),  sort = 'A', text_color='moccasin' ))

                itemlist.append(Item( channel='search', action='search', search_type='all', title='[B]Buscar Solo en los canales de esta agrupación ...[/B]',
                                      context=context_buscar, only_channels_group = canales, group = item.group, only = item.only, search_special = item.search_special,
                                      thumbnail=config.get_thumb('search'), sort = 'B', text_color='yellowgreen' ))

    return sorted(itemlist, key=lambda it: it.sort)


def ch_generos(item):
    return ch_groups(item)


def idioma_canal(lang):
    idiomas = { 'cast': 'Castellano', 'lat': 'Latino', 'eng': 'Inglés', 'pt': 'Portugués', 'vo': 'VO', 'vose': 'Vose', 'vos': 'Vos', 'cat': 'Català' }
    return idiomas[lang] if lang in idiomas else lang


def _marcar_canal(item):
    from modules import submnuctext
    submnuctext._marcar_canal(item)


def _quitar_proxies(item):
    from modules import submnuctext
    submnuctext._quitar_proxies(item)


def _dominio_vigente(item):
    from modules import submnuctext
    submnuctext._dominio_vigente(item)


def _dominio_memorizado(item):
    from modules import submnuctext
    submnuctext._dominio_memorizado(item)


def _dominios(item):
    from modules import submnuctext
    submnuctext._dominios(item)


def _credenciales(item):
    from modules import submnuctext
    submnuctext._credenciales(item)


def _proxies(item):
    from modules import submnuctext
    submnuctext._proxies(item)


def _tests(item):
    from modules import submnuctext
    submnuctext._test_webs(item)
