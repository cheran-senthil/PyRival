" Line numbering, highlight search, mouse in insert mode 
set number
set hlsearch
set mouse=a

" 4-space indent using spaces
set autoindent
set expandtab
set smarttab
set shiftwidth=4
set softtabstop=4
set tabstop=4

" Indent keys: Shift+Tab unindents; Tab indents (overriding <C-i> in normal mode)
inoremap <S-Tab> <C-d>
nnoremap <S-Tab> <<
nnoremap <Tab> >>
vnoremap <Tab> >gv
vnoremap <S-Tab> <gv

" Colors, disable flash on error
colorscheme desert
set novisualbell
