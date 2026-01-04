def funct(root) : 

    pre = []
    In = []
    post = []

    if root is None : 
        return [pre, In, post]

    st = []
    st.append({root, 1})

    while st : 

        elem = st.pop()
        
        if elem.freq == 1 :
            pre.append(elem.key.val)
            st.append({elem.key, 2})

            if elem.key.left : 
                st.append({elem.key.left, 1})

        elif elem.freq == 2 :
            In.append(elem.key.val)
            st.append({elem.key, 3})

            if elem.key.right : 
                st.append({elem.key.right, 1})
        else : 
            post.append(elem.key.val)


    return [pre, In, post]

    