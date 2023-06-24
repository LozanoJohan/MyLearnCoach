import streamlit as st

def home_page(view):
    query = ''

    st.balloons()
    prompt = st.text_input('¿En que te puedo ayudar?') 
    
    if prompt:
        response = view.controller.process_input(prompt)

        st.write(response['title'])

        coursera_courses, keywords = view.controller.get_coursera_courses(response["script"])

        print('First keyword: ', keywords[0], 'Keyword:', keywords)

        st.markdown(f'<h2>Cursos recomendados acerca de {keywords[0]}</h2>', unsafe_allow_html=True)
        st.subheader('Coursera')

        if len(coursera_courses) == 0:
            st.write("No se encontraron cursos")

        # Mostrar todos los cursos en 3 columnas
        i = 0

        for rows in range(len(coursera_courses)//3 + 1):
            for col in st.columns(3):
                # Escribir nombre y código
                try:
                    col.markdown(f'''**{coursera_courses[i].name}** <br>
                                ---------------------------------------------------------------<br>
                                Puntaje: {coursera_courses[i].score}<br>
                                Reseñas: {coursera_courses[i].reviews}<br>
                                url: {coursera_courses[i].url}''', unsafe_allow_html=True)
                except:
                    continue
                
                i += 1

            st.divider()
    
    else:
        st.markdown(f'<h2>Cursos recomendados acerca de </h2>', unsafe_allow_html=True)

        st.subheader('Coursera')
        st.write('Parece que aún no me has preguntado nada')

        st.subheader('SIA')
        st.write('Parece que aún no me has preguntado nada')

    # Sección de cursos
    col1, col2 = st.columns(2)
    col1.header("Cursos")

    with col2:
        sub_col1, sub_col2 = st.columns(2)
        query_type = sub_col1.selectbox("Buscar por:", ["----", "Nombre", "Código"])
        query = sub_col2.text_input("", query, placeholder='🔎 Buscar')

    school_box, carreer_box, update_btn = st.columns(3)

    school_box.selectbox('Facultad', ['----', 'Facultad de Ingeniería', 'Facultad de Ciencias Econámicas', 'Facultad de Ciencias de la Computación', 'Facultad de Ciencias Sociales'])
    carreer_box.selectbox('Carrera', ['----', 'Ingeniería', 'Ciencias Econámicas', 'Ciencias de la Computación', 'Ciencias Sociales'])
    update_btn.write('--')
    update_btn.button("Actualizar", on_click=view.controller.fetch_sia_courses)
    
    sia_courses = view.controller.get_sia_courses(query_type, query)
    # Mostrar todos los cursos en 3 columnas
    i = 0

    for rows in range(len(sia_courses)//3 + 1):
        for col in st.columns(3):
            # Escribir nombre y código
            try:
                col.markdown(f'''**{sia_courses[i].name}** {sia_courses[i].code}<br>
                             ---------------------------------------------------------------<br>
                             Créditos: {sia_courses[i].credits}<br>
                             Tipología: {sia_courses[i].type}''', unsafe_allow_html=True)
            except:
                continue
            
            i += 1

        st.divider()