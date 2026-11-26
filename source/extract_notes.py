import zipfile,re,sys,glob,os
out=sys.argv[1]
for f in sorted(glob.glob('0*.docx')):
    z=zipfile.ZipFile(f)
    x=z.read('word/document.xml').decode('utf8')
    paras=re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S)
    lines=[]
    for p in paras:
        st=re.search(r'<w:pStyle w:val="([^"]+)"',p)
        t=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
        if t.strip():
            pre='#'*int(st.group(1)[-1])+' ' if st and st.group(1).startswith('Heading') and st.group(1)[-1].isdigit() else ''
            lines.append(pre+t)
    open(os.path.join(out,f[:2]+'.txt'),'w',encoding='utf8').write('\n'.join(lines))
    print(f,len(lines),sum(len(l) for l in lines))
