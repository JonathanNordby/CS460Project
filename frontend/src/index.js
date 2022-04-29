import { createRoot } from 'react-dom/client';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import F1F2 from './routes/f1_f2';
import F3 from './routes/f3';
import F4 from './routes/f4';
import F6 from './routes/f6';
import SignIn from './routes/SignIn';
import { AuthProvider } from 'react-auth-kit'

const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <AuthProvider authType = {'cookie'}
    authName={'_auth'}
    cookieDomain={window.location.hostname}
    cookieSecure={window.location.protocol === "https:"}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="f1_f2" element={<F1F2 />} />
        <Route path="f3" element={<F3 />} />
        <Route path="f4" element={<F4 />} />
        <Route path="f6" element={<F6 />} />
        <Route path="sign_in" element={<SignIn />} />
      </Routes>
    </BrowserRouter>
  </AuthProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
