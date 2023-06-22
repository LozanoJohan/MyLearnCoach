import streamlit as st

def events_page():
    st.snow()
    st.markdown('''<style>
    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }

    th {
      background-color: #f2f2f2;
    }
  </style>

  <h2>Tu horario</h2>
  <table>
    <tr>
      <th>Tiempo</th>
      <th>Lunes</th>
      <th>Martes</th>
      <th>Miercoles</th>
      <th>Jueves</th>
      <th>Viernes</th>
      <th>Sabado</th>
      <th>Domingo</th>
    </tr>
    <tr>
      <td>5:00 am-7:00 am</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>7:00 am-9:00 am</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>9:00 am-11:00 am</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>11:00 am-1:00 pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>1:00 pm-3:00 pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>3:00pm-5:00pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>5:00pm-7:00pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>7:00pm-9:00pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
    <tr>
      <td>9:00pm-11:00pm</td>
      <td>Task 2</td>
      <td>Task 3</td>
      <td>Task 4</td>
      <td>Task 5</td>
      <td>Task 6</td>
      <td>Task 7</td>
      <td>Task 7</td>
    </tr>
  </table>''', unsafe_allow_html=True)
    
    st.header('Próximos eventos')
    st.markdown('- Evento 1')
    st.markdown('- Evento 1')
    st.markdown('- Evento 1')
    st.markdown('- Evento 1')