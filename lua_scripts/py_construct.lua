ZomLoad({File={Path="C:\Users\MAshp\AppData\Local\Temp\rizom_temp.fbx", ImportGroups=true, XYZ=true}, NormalizeUVW=true})ZomIslandGroups({Mode='SetGroupsProperties', WorkingSet='Visible', MergingPolicy=8322, GroupPaths={ 'RootGroup' }, Properties={Pack={SpacingSize=0.0078125}}})ZomIslandGroups({Mode='SetGroupsProperties', WorkingSet='Visible', MergingPolicy=8322, GroupPaths={ 'RootGroup' }, Properties={Pack={MarginSize=0.0078125}}})ZomSet({Path='Prefs.PackOptions.MapResolution', Value=2048})ZomSet({Path="Vars.EditMode.ElementMode", Value=1})
ZomSelect({PrimType="Edge", WorkingSet="Visible", Select=true, All=true})
ZomSelect({PrimType="Edge", WorkingSet="Visible", Select=true, ResetBefore=true, ProtectMapName="Protect", FilterIslandVisible=true, Auto={SharpEdges={AngleMin=70}, PipesCutter=false, HandleCutter=true, StoreCoordsUVW=true, FlatteningMode=0, FlatteningUnfoldParams={Iterations=1, BorderIntersections=true, TriangleFlips=true}}})
ZomCut({PrimType="Edge", WorkingSet="Visible"})
ZomLoad({Data={CoordsUVWInternalPath="Mesh.Tmp.AutoSelect.UVW"}})
ZomIslandGroups({Mode="DistributeInTilesByBBox", WorkingSet="Visible", MergingPolicy=8322})
ZomIslandGroups({Mode="DistributeInTilesEvenly", WorkingSet="Visible", MergingPolicy=8322, UseTileLocks=true, UseIslandLocks=true})
ZomPack({ProcessTileSelection=false, RecursionDepth=1, RootGroup="RootGroup", WorkingSet="Visible", Scaling={Mode=2}, Rotate={}, Translate=true, LayoutScalingMode=2})