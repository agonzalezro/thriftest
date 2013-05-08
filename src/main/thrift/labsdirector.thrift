namespace java com.cloud9ers.director
namespace rb director

exception ThisIsSparta {
	1: string message
}

service LabsDirector {
	string hello(1: string name);
    void bye() throws(1: ThisIsSparta ex);
}
