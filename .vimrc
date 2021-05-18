" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')


" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plug 'junegunn/vim-easy-align'

"Surround.vim is all about : parentheses, brackets, quotes, XML
"tags, and more. The plugin provides mappings to easily delete, change and add
"such surroundings in pairs.
Plug 'tpope/vim-surround'

"a nice statusline at the bottom of each vim window
Plug 'vim-airline/vim-airline'

"NERDTree (file explorer for vim)
Plug 'scrooloose/nerdtree'

"syntax checking
Plug 'scrooloose/syntastic'

"Sonokai Color scheme

Plug 'sainnhe/sonokai'
"vim airline themes

Plug 'vim-airline/vim-airline-themes'

"syntax checking using lsp support

Plug 'w0rp/ale'

"markdown preview

Plug 'instant-markdown/vim-instant-markdown', {'for': 'markdown'}

" Initialize plugin system
 call plug#end()

colorscheme sonokai
