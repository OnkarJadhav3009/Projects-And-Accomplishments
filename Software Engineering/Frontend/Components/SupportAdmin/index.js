import React from 'react';

import { ChatEngine } from 'react-chat-engine'

const SupportAdmin = () => {
  return (
    <ChatEngine 
      projectID={"eb28d730-4e68-4849-adbc-3c2fb982b7a3"}
      userName={'WatchaFlick'}
      userSecret={'watchaflick@123'}
      height='calc(100vh - 12px)'
    />
  );
}

export default SupportAdmin;
