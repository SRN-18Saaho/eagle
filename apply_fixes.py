p='app.src.html'
s=open(p,encoding='utf-8').read()
E=[]
def r(old,new): E.append((old,new))

r(r'''<title>CampusConnect · VESIT</title>''', r'''<title>CampusConnect · VESIT</title>
<link rel="icon" href="__LOGO_IMG__">''')
r(r'''.ac{background:var(--ac);color:#fff} .acx{color:var(--ac)}
</style>''', r'''.ac{background:var(--ac);color:#fff} .acx{color:var(--ac)}
button:focus-visible,select:focus-visible,a:focus-visible{outline:2px solid var(--ac);outline-offset:2px}
</style>''')
r(r'''ask the placement cell first."}]
};''', r'''ask the placement cell first."}],
  4:[{who:"Karan · 3rd Year ECS",senior:true,time:"8h ago",text:"I have done embedded and VLSI projects in ECS. Reply with your branch and year and I will get in touch."}]
};
POSTS.forEach(p=>{ p.comments = (SEED[p.id]||[]).length; });   // keep the count equal to the replies shown''')
r(r'''const COLLEGE_DOMAIN = "ves.ac.in";''', r'''const COLLEGE_DOMAIN = "ves.ac.in";
const EMAIL_RE = new RegExp("^[^\\s@]+@"+COLLEGE_DOMAIN.replace(/\./g,"\\.")+"$","i");   // exactly one @, ends with the college domain
const LOGO = "__LOGO_IMG__";
const niceName = email => {   // "2026.abhinav.gurav@ves.ac.in" -> "Abhinav Gurav"
  const parts = email.split("@")[0].split(/[._-]+/).filter(x=>x && !/^\d+$/.test(x));
  return parts.length ? parts.map(x=>x[0].toUpperCase()+x.slice(1)).join(" ") : "there";
};''')
r(r'''<div className="w-9 h-9 rounded-full ac flex items-center justify-center font-extrabold">C</div>
    <div className="leading-tight">''', r'''<img src={LOGO} alt="VESIT logo" className="h-10 w-auto rounded-md bg-white p-0.5 border bdr"/>
    <div className="leading-tight hidden sm:block">''')
r(r'''placeholder="Search questions" className=''', r'''placeholder="Search questions" aria-label="Search questions" className=''')
r(r'''<button onClick={()=>setDark(!dark)} className="w-10 h-10 rounded-full hv text-lg">''', r'''<button onClick={()=>setDark(!dark)} aria-label={dark?"Switch to light mode":"Switch to dark mode"} className="w-10 h-10 rounded-full hv text-lg">''')
r(r'''className="relative w-10 h-10 rounded-full hv text-lg">🔔''', r'''aria-label="Hackathon alerts" className="relative w-10 h-10 rounded-full hv text-lg">🔔''')
r(r'''className="w-10 h-10 rounded-full ac text-lg">🎓</button>''', r'''aria-label="Account menu" className="w-10 h-10 rounded-full ac text-lg">🎓</button>''')
r(r'''          {bell && (
            <div className="card absolute right-0 top-14 w-80 max-w-[85vw] p-5 shadow-xl">''', r'''          {(bell||menu) && <div className="fixed inset-0 z-30" onClick={()=>{setBell(false);setMenu(false)}}/>}
          {bell && (
            <div className="card absolute right-0 top-14 z-40 w-80 max-w-[85vw] p-5 shadow-xl">''')
r(r'''<div className="card absolute right-0 top-14 w-64 p-5 shadow-xl">''', r'''<div className="card absolute right-0 top-14 z-40 w-64 max-w-[85vw] p-5 shadow-xl">''')
r(r'''<img src={img.src} alt="" className=''', r'''<img src={img.src} alt="Attached image" className=''')
r(r'''if(ai && !ai.loading) return setAi(null);          // second click hides it''', r'''if(ai&&ai.loading) return;                          // ignore clicks while an answer is loading
    if(ai) return setAi(null);                          // second click hides it''')
r(r'''<button onClick={()=>setVote(vote===1?0:1)} className=''', r'''<button onClick={()=>setVote(vote===1?0:1)} aria-label="Upvote" className=''')
r(r'''<button onClick={()=>setVote(vote===-1?0:-1)} className=''', r'''<button onClick={()=>setVote(vote===-1?0:-1)} aria-label="Downvote" className=''')
r(r'''<button onClick={()=>setOpen(!open)} className="px-3 py-1.5 rounded-full hv t2 text-xs font-semibold">💬 {p.comments+list.length-seed.length} {open?"· Hide":"· Reply"}</button>''', r'''<button onClick={()=>setOpen(!open)} aria-expanded={open} className="px-3 py-1.5 rounded-full hv t2 text-xs font-semibold">💬 {list.length} {open?"· Hide":"· Reply"}</button>''')
r(r'''<Tip label={saved?"Saved":"Save"}><button onClick={()=>setSaved(!saved)} className=''', r'''<Tip label={saved?"Saved":"Save"}><button onClick={()=>setSaved(!saved)} aria-label="Save post" className=''')
r(r'''<button onClick={share} className=''', r'''<button onClick={share} aria-label="Copy link" className=''')
r(r'''placeholder="Write a reply..." className="inp flex-1 rounded-full px-5 py-2.5 text-sm"/>''', r'''placeholder="Write a reply..." maxLength={500} aria-label="Write a reply" className="inp flex-1 rounded-full px-5 py-2.5 text-sm"/>''')
r(r'''function Composer({onPost}) {
  const [draft,setDraft] = useState("");''', r'''function Composer({onPost,tag}) {
  const [draft,setDraft] = useState("");
  const [cat,setCat] = useState(tag==="All"?"DSA":tag);''')
r(r'''const pick = e => { const f=e.target.files[0]; if(f) setImg({src:URL.createObjectURL(f)}); };''', r'''const pick = e => { const f=e.target.files[0]; if(f) setImg({src:URL.createObjectURL(f)}); e.target.value=""; };   // reset so the same file can be picked again''')
r(r'''onPost(draft.trim(),img); setDraft(""); setImg(null);''', r'''onPost(draft.trim(),img,cat); setDraft(""); setImg(null);''')
r(r'''<div className="flex items-center gap-4">
        <span className="w-10 h-10 rounded-full bgh flex items-center justify-center shrink-0">👤</span>''', r'''<div className="flex items-center gap-3 flex-wrap">
        <span className="w-10 h-10 rounded-full bgh flex items-center justify-center shrink-0">👤</span>''')
r(r'''placeholder="Ask your seniors anonymously..." className="inp flex-1 rounded-full px-5 py-3 text-sm"/>''', r'''placeholder="Ask your seniors anonymously..." maxLength={200} aria-label="Your question" className="inp flex-1 min-w-[10rem] rounded-full px-5 py-3 text-sm"/>''')
r(r'''<button onClick={post} className="ac rounded-full px-6 py-2.5 text-sm font-bold">Post</button>''', r'''<select value={cat} onChange={e=>setCat(e.target.value)} aria-label="Community" className="inp rounded-full px-3 py-2.5 text-xs font-semibold">{Object.keys(TAGS).map(t=><option key={t} value={t}>c/{t}</option>)}</select>
        <button onClick={post} className="ac rounded-full px-6 py-2.5 text-sm font-bold">Post</button>''')
r(r'''function Feed({q,tag,setTag}) {''', r'''function Feed({q,setQ,tag,setTag}) {''')
r(r'''const add = (title,img) => setPosts([{id:Date.now(),age:0,time:"just now",tag:tag==="All"?"DSA":tag,votes:1,comments:0,autoAI:true,title,body:"",img,summary:[["Status","No answers yet. Seniors will reply soon."]]},...posts]);''', r'''const add = (title,img,cat) => {
    setPosts([{id:Date.now(),age:0,time:"just now",tag:cat,votes:1,comments:0,autoAI:true,title,body:"",img,summary:[["Demo","No Gemini key is set, so this is a placeholder. Add your key in the file for a real AI answer."]]},...posts]);
    setTag(cat); setQ(""); setSort("New");        // make sure the new post is visible at the top
  };''')
r(r'''<Composer onPost={add}/>''', r'''<Composer onPost={add} tag={tag}/>''')
r(r'''const Profile = ({branch,setBranch}) => (''', r'''const Profile = ({user,branch,setBranch}) => (''')
r(r'''🛡️ Verified Senior Mentor''', r'''🛡️ Verified VESIT student''')
r(r'''<div className="h-3 w-28 rounded bgh mt-5" title="Identity hidden"/>''', r'''<div className="text-xl font-extrabold mt-5">{niceName(user)}</div>
      <div className="text-xs t2 mt-1 break-all">{user}</div>''')
r(r'''const name = user.split("@")[0];''', r'''const name = niceName(user);''')
r(r'''const submit = () => {
    const e = email.trim().toLowerCase();''', r'''const submit = () => {
    if(sent) return;                           // ignore double clicks
    const e = email.trim().toLowerCase();''')
r(r'''if(!e.endsWith("@"+COLLEGE_DOMAIN) || e.length <= COLLEGE_DOMAIN.length+1)''', r'''if(!EMAIL_RE.test(e))''')
r(r'''<div className="w-11 h-11 rounded-full ac flex items-center justify-center font-extrabold text-lg">C</div>''', r'''<img src={LOGO} alt="VESIT logo" className="h-20 w-auto self-start rounded-xl bg-white p-1.5 shadow-lg"/>''')
r(r'''title="Toggle theme">''', r'''title="Toggle theme" aria-label="Toggle theme">''')
r(r'''<label className="block text-sm font-semibold mt-7">College email</label>''', r'''<label htmlFor="em" className="block text-sm font-semibold mt-7">College email</label>''')
r(r'''placeholder={"name@"+COLLEGE_DOMAIN} className="inp w-full mt-2 rounded-xl px-4 py-3 text-sm"/>''', r'''id="em" autoComplete="username" placeholder={"name@"+COLLEGE_DOMAIN} className="inp w-full mt-2 rounded-xl px-4 py-3 text-sm"/>''')
r(r'''<label className="block text-sm font-semibold mt-5">Password</label>''', r'''<label htmlFor="pw" className="block text-sm font-semibold mt-5">Password</label>''')
r(r'''placeholder="Enter your password" autoComplete="current-password"''', r'''id="pw" placeholder="Enter your password" autoComplete="current-password"''')
r(r'''{error && <p className="text-sm text-red-500 mt-3">{error}</p>}''', r'''{error && <p role="alert" className="text-sm text-red-500 mt-3">{error}</p>}''')
r(r'''const [user,setUser] = useState(null);''', r'''const [user,setUser] = useState(()=>{ try{ const u=localStorage.getItem("cc-user"); return u&&EMAIL_RE.test(u)?u:null; }catch(e){ return null; } });   // stays signed in after refresh (demo only)''')
r(r'''const [branch,setBranch] = useState("COMP");
  if(!user) return <Login onLogin={(e,b)=>{setUser(e);setBranch(b)}} dark={dark} setDark={setDark}/>;''', r'''const [branch,setBranch] = useState(()=>{ try{ const b=localStorage.getItem("cc-branch"); if(b&&BR[b]) return b; }catch(e){} return "COMP"; });
  useEffect(()=>{ try{ if(user) localStorage.setItem("cc-user",user); else localStorage.removeItem("cc-user"); localStorage.setItem("cc-branch",branch); }catch(e){} },[user,branch]);
  useEffect(()=>{ window.scrollTo(0,0); },[page]);   // new page starts at the top
  if(!user) return <Login onLogin={(e,b)=>{setUser(e);setBranch(b)}} dark={dark} setDark={setDark}/>;''')
r(r'''onLogout={()=>{setUser(null);setPage("home")}}''', r'''onLogout={()=>{setUser(null);setPage("home");setQ("");setTag("All")}}''')
r(r'''{withRail && <Feed q={q} tag={tag} setTag={setTag}/>}''', r'''{withRail && <Feed q={q} setQ={setQ} tag={tag} setTag={setTag}/>}''')
r(r'''<Profile branch={branch} setBranch={setBranch}/>''', r'''<Profile user={user} branch={branch} setBranch={setBranch}/>''')

for old,new in E:
    c=s.count(old)
    assert c==1,(c,old[:70])
    s=s.replace(old,new)
open(p,'w',encoding='utf-8').write(s)
print("applied",len(E))
