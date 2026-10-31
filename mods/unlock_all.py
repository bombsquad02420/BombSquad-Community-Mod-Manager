import bs
import bsInternal
import bsUtils

# Every store unlock in 1.4 (characters, maps, extra game types, pro) is checked
# through bsInternal._getPurchased, and custom playlists / pro game options through
# bsUtils._haveProOptions. Both are always looked up by module attribute, so
# replacing them here takes effect everywhere. This only changes what this client
# shows; anything the account server checks (tickets, tournaments) is unaffected.

_supports_auto_reloading = True
_auto_reloader_type = "patching"
_getPurchased = bsInternal._getPurchased
_haveProOptions = bsUtils._haveProOptions


def _prepare_reload():
    bsInternal._getPurchased = _getPurchased
    bsUtils._haveProOptions = _haveProOptions


def getPurchased(item):
    return True


def haveProOptions():
    return True


bsInternal._getPurchased = getPurchased
bsUtils._haveProOptions = haveProOptions
