namespace java com.cloud9ers.director
namespace rb director

exception InstanceDoesNotExist {
	1: string description
}

service LabsDirector {
	void hello(1: string name) throws(1: InstanceDoesNotExist ex);
}
